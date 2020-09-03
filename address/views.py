from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import AddressSerializer
from .models import Address
from .permissions import IsOwner

# Create your views here.

# AddressListAPIView
class AddressListAPIView(ListCreateAPIView):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(add_owner = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(add_owner = self.request.user)

# AddressDetailAPIView
class AddressDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    lookup_field = 'id'

    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return self.queryset.filter(add_owner = self.request.user)