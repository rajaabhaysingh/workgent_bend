from django.db import models
from django_mysql.models import JSONField
import uuid

from authentication.models import User

# -------------- MY JOBS --------------

# Job
class Job(models.Model):

    JOB_TYPES=[
        ('NORMAL', 'NORMAL'),
        ('BULK', 'BULK'),
        ('EVENT', 'EVENT'),
        ('OTHER', 'OTHER'),
    ]

    PAY_UNITS=[
        ('Minute', 'Minute'),
        ('Hour', 'Hour'),
        ('Day', 'Day'),
        ('Month', 'Month'),
        ('Year', 'Year'),
        ('TASK', 'TASK'),
    ]

    COUNTRIES = [
        ('INDIA', 'INDIA'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_type = models.CharField(choices=JOB_TYPES, max_length=64)
    job_name = models.CharField(max_length=64)
    job_owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='job_owner')
    job_desc = models.TextField(null=True, blank=True)
    job_details = JSONField(null=True, blank=True)
    job_img = models.ImageField(upload_to='jobs/%Y/%m/', max_length=1024, null=True, blank=True)
    job_duration = models.DecimalField(max_digits=10, decimal_places=2)
    is_permanent = models.BooleanField(default=False)
    req_qty = models.PositiveIntegerField()
    pay_amt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pay_amt_unit = models.CharField(choices=PAY_UNITS, max_length=64, null=True, blank=True)
    is_negotiable = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_accom_avail = models.BooleanField(default=False)
    is_ad = models.BooleanField(default=False)
    qty_filled = models.PositiveIntegerField(default=0)
    add_line = models.CharField(max_length=1024)
    country = models.CharField(choices=COUNTRIES, max_length=64, null=True, blank=True)
    div_1_state = models.CharField(max_length=64, null=True, blank=True)
    div_2_dist = models.CharField(max_length=64, null=True, blank=True)
    div_3_subdist = models.CharField(max_length=64, null=True, blank=True)
    div_4_vill_colony = models.CharField(max_length=64, null=True, blank=True)
    zip = models.PositiveIntegerField()
    lat = models.DecimalField(max_digits=23, decimal_places=20, null=True, blank=True)
    long = models.DecimalField(max_digits=23, decimal_places=20, null=True, blank=True)

    class Meta:
        ordering: ['-posted_at']

    def __str__(self):
        return (str(self.job_name)+ ', owner id: ' + str(self.job_owner))
