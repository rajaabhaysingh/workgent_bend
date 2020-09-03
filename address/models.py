from django.db import models
from authentication.models import User
import uuid

class Address(models.Model):

    COUNTRIES = [
        ('INDIA', 'INDIA'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    add_owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    add_line = models.CharField(max_length=1024)
    country = models.CharField(choices=COUNTRIES, max_length=64)
    div_1_state = models.CharField(max_length=64)
    div_2_dist = models.CharField(max_length=64)
    div_3_subdist = models.CharField(max_length=64, null=True, blank=True)
    div_4_vill_colony = models.CharField(max_length=64, null=True, blank=True)
    zip = models.PositiveIntegerField()
    lat = models.DecimalField(max_digits=23, decimal_places=20, null=True, blank=True)
    long = models.DecimalField(max_digits=23, decimal_places=20, null=True, blank=True)

    class Meta:
        ordering: ['-id']

    def __str__(self):
        return (str(self.add_line)+ ', zip: ' + str(self.zip))