from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import datetime
from jobs.models import Job
from rest_framework import status
from rest_framework.response import Response

from .permissions import IsOwner

# Create your views here.

class PostedJobStatsAPIView(APIView):

    # permission_classes = (IsAuthenticated, IsOwner)

    def get_people_recruited(self, job_list, category):
        jobs = job_list.filter(job_type=category)
        quantity = 0

        for job in jobs:
            quantity += job.req_qty

        return {'quantity': str(quantity)}

    def get_categories(self, job):
        return job.job_type

    def get(self, request):
        todays_date = datetime.date.today()
        month_ago =  todays_date - datetime.timedelta(days=30)
        jobs = Job.objects.filter(job_owner=request.user, posted_at__gt=month_ago)
        final = {}
        categories = list(set(map(self.get_categories, jobs)))

        for job in jobs:
            for category in categories:
                final[category] = self.get_people_recruited(jobs, category)

        return Response({'category_data': final}, status=status.HTTP_200_OK)