from rest_framework import serializers

from .models import Job

# JobSerializer
class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ['id','job_type', "job_name", "job_img", "job_desc", "job_details", "job_duration", "is_permanent", "req_qty", "pay_amt", "pay_amt_unit", "is_negotiable", "add_line", "country", "div_1_state", "div_2_dist", "div_3_subdist", "div_4_vill_colony", "zip", "lat", "long"]

# PublicJobSerializer
class PublicJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ['id','job_type', "job_name", "job_img", 'job_owner', "job_desc", "job_duration", "is_permanent", "req_qty", "pay_amt", "pay_amt_unit", "is_negotiable", "posted_at", 'is_accom_avail', "is_ad", "qty_filled", "div_3_subdist", "div_4_vill_colony", "zip", "lat", "long"]

