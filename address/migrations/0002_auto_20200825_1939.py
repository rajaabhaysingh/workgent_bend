# Generated by Django 3.1 on 2020-08-25 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='add_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='div_3_subdist',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='div_4_vill_colony',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=23, null=True),
        ),
    ]
