# Generated by Django 3.0.5 on 2020-08-26 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20200826_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='applicants',
        ),
    ]
