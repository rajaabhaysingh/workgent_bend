from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, RequestPasswordResetEmail, PasswordTokenCheckAPIView, SetNewPasswordAPIView
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"), 
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"), 
    path('request-reset-password-email/', RequestPasswordResetEmail.as_view(), name="request-reset-password-email"), 
    path('reset-password/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name="reset-password-confirm"), 
    path('reset-password-final', SetNewPasswordAPIView.as_view(), name="reset-password-final"), 
]