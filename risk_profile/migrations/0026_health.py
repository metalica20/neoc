# Generated by Django 2.1.5 on 2019-03-24 05:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0025_settlements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('operator_type', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('opening_hours', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('phone_number', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('email_address', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('emergency_service', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default=None, max_length=50, null=True)),
                ('icu', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default=None, max_length=50, null=True)),
                ('nicu', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default=None, max_length=50, null=True)),
                ('operating_theatre', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default=None, max_length=50, null=True)),
                ('x_ray', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default=None, max_length=50, null=True)),
                ('ambulance_service', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default=None, max_length=50, null=True)),
                ('number_of_staff', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('number_of_Beds', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('Comments', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('lat', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('long', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326)),
            ],
        ),
    ]
