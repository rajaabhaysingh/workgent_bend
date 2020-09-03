from rest_framework import serializers

from .models import Address

# AddressSerializer
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ["id", "add_line", "country", "div_1_state", "div_2_dist", "div_3_subdist", "div_4_vill_colony", "zip", "lat", "long"]