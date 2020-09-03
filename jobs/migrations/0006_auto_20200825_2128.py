# Generated by Django 3.0.5 on 2020-08-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_job_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_address',
        ),
        migrations.AddField(
            model_name='job',
            name='add_line',
            field=models.CharField(default='Aliganj', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='country',
            field=models.CharField(blank=True, choices=[('INDIA', 'INDIA')], max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='div_1_state',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='div_2_dist',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='div_3_subdist',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='div_4_vill_colony',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=23, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=23, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='zip',
            field=models.PositiveIntegerField(default=812005),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_img',
            field=models.ImageField(blank=True, max_length=1024, null=True, upload_to='jobs/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='job',
            name='pay_amt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pay_amt_unit',
            field=models.CharField(blank=True, choices=[('Minute', 'Minute'), ('Hour', 'Hour'), ('Day', 'Day'), ('Month', 'Month'), ('Year', 'Year'), ('TASK', 'TASK')], max_length=64, null=True),
        ),
    ]
