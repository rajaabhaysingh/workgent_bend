from django.urls import path
from .views import PostedJobStatsAPIView

urlpatterns = [
    path('my/', PostedJobStatsAPIView.as_view(), name="my-stats"),
]