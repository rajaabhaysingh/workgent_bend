from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .models import User

# RegisterSerializer
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=68, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'picture']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        # if not username.isalnum():
        #     raise serializers.ValidationError('Username should only contain alphanumeric characters.')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# EmailVerificationSerializer
class EmailVerificationSerializer(serializers.ModelSerializer):

    token = serializers.CharField(max_length=1024)

    class Meta:
        model = User
        fields = ['token']

# LoginSerializer
class LoginSerializer(serializers.ModelSerializer):

    # email = serializers.EmailField(max_length=255, min_length=3, write_only=True)
    password = serializers.CharField(max_length=255, min_length=1, write_only=True)
    username = serializers.CharField(max_length=255, min_length=1)
    tokens = serializers.CharField(max_length=1024, min_length=1, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'tokens', 'picture']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        user = auth.authenticate(username =  username, password = password)

        if not user:
            raise AuthenticationFailed('Inavlid credentials.')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled. Contact us for further help.')

        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified.')

        return {
            'id': user.id,
            # 'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
            'picture': user.picture
        }

# RequestPasswordResetEmailSerializer
class RequestPasswordResetEmailSerializer(serializers.Serializer):
    
    email = serializers.EmailField(max_length=255, min_length=3)

    class Meta:
        fields = ['email']

# SetNewPasswordSerializer
class SetNewPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    token = serializers.CharField(max_length=1024, write_only=True)
    uidb64 = serializers.CharField(max_length=1024, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        
        try:
            password = attrs.get('password', '')
            token = attrs.get('token', '')
            uidb64 = attrs.get('uidb64', '')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('Password reset link has expired. Try resetting password again to get new link.', 401)

            user.set_password(password)
            user.save()
            return (user)

        except Exception as e:
            raise AuthenticationFailed('Password reset link is invalid/tempered. Try resetting password again to get new link.', 401)