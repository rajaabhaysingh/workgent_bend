# Generated by Django 3.0.5 on 2020-10-18 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_remove_job_applicants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_details',
        ),
    ]
