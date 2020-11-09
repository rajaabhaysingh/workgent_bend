from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# UserManager
class UserManager(BaseUserManager):

    def create_user(self, username, email, picture=None, password=None):

        if username is None:
            raise TypeError("Username cannot be empty")
        if email is None:
            raise TypeError("Email cannot be empty")

        user = self.model(username = username, email = self.normalize_email(email), picture = picture)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, picture=None, password=None):

        if password is None:
            raise TypeError("Password cannot be empty")

        user = self.create_user(username, email, picture, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

# User
class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    picture = models.ImageField(upload_to='dp/%Y/%m/', max_length=1024, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        