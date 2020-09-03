from django.urls import path
from .views import AddressListAPIView, AddressDetailAPIView

urlpatterns = [
    path('my/', AddressListAPIView.as_view(), name="address-list-private"),
    path('my/<int:id>/', AddressDetailAPIView.as_view(), name="address-detail-private"),
]