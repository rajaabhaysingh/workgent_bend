# Generated by Django 3.1 on 2020-08-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_qty_filled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='qty_filled',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
