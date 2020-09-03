from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from .serializers import JobSerializer, PublicJobSerializer
from .models import Job
from .permissions import IsOwner
from .mixins import MyPaginationMixin

# Create your views here.

# PublicJobListAPIView
class PublicJobListAPIView(APIView, MyPaginationMixin):

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request):
        queryset = Job.objects.all()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = PublicJobSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

# PublicJobDetailAPIView
class PublicJobDetailAPIView(APIView):

    lookup_field = 'id'

    def get_object(self, id):
        try:
            return Job.objects.get(id=id)

        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        job = self.get_object(id)
        serializer = JobSerializer(job)
        return Response(serializer.data)

# JobListAPIView
class JobListAPIView(ListCreateAPIView):

    serializer_class = JobSerializer
    queryset = Job.objects.all()

    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(job_owner = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(job_owner = self.request.user)

# JobDetailAPIView
class JobDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = JobSerializer
    queryset = Job.objects.all()

    lookup_field = 'id'

    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return self.queryset.filter(job_owner = self.request.user)