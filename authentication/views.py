from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, RequestPasswordResetEmailSerializer, SetNewPasswordSerializer
from .models import User
from .utils import Util
from .renderers import UserRenderer

# Create your views here.

# RegisterView
class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email = user_data['email'])

        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl = 'http://' + current_site + relativeLink + '?token=' + str(token)
        email_body = 'Hi ' + user.username + ', \n\nnPlease click the link below to verify your email-id \n\n' + absurl + '\n\nYou are receiving this email because, you signed up at workgent.ml\n\n--\nTeam workgent\nwww.workgent.ml'
        data = {'email_body': email_body, 'email_to': user.email, 'email_subject': 'Verify your email - Workgent'}

        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)

# VerifyEmail
class VerifyEmail(views.APIView):

    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Email verification token', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id = payload['user_id'])

            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation token expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

# LoginAPIView
class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# RequestPasswordResetEmail
class RequestPasswordResetEmail(generics.GenericAPIView):

    serializer_class = RequestPasswordResetEmailSerializer

    def post(self, request):

        # data = {'request': request, 'data' : request.data}
        serializer = self.serializer_class(data=request.data)

        email = request.data['email']
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request=request).domain
            relativeLink = reverse('reset-password-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + current_site + relativeLink
            email_body = 'Hi, \n\nPlease use the link below to reset your password \n\n' + absurl + '\n\n--\nTeam workgent\nwww.workgent.ml'
            data = {'email_body': email_body, 'email_to': user.email, 'email_subject': 'Reset password - Workgent'}

            Util.send_email(data)

        return Response({'success': 'Password reset link sent to your email-id. Please check your inbox.'}, status=status.HTTP_200_OK)

# PasswordTokenCheckAPIView
class PasswordTokenCheckAPIView(generics.GenericAPIView):

    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Password reset link has expired. Try resetting password again to get new link.'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'message': 'Credentials valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            return Response({'error': 'Password reset link is invalid/tempered. Try resetting password again to get new link.'}, status=status.HTTP_401_UNAUTHORIZED)

# SetNewPasswordAPIView
class SetNewPasswordAPIView(generics.GenericAPIView):

    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'success': True, 'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)