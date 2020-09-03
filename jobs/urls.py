from django.urls import path
from .views import JobListAPIView, JobDetailAPIView, PublicJobListAPIView, PublicJobDetailAPIView

urlpatterns = [
    path('', PublicJobListAPIView.as_view(), name="job-list-public"),
    path('<int:id>/', PublicJobDetailAPIView.as_view(), name="job-detail-public"),
    path('my/', JobListAPIView.as_view(), name="job-list-private"),
    path('my/<int:id>/', JobDetailAPIView.as_view(), name="job-detail-private"),
]