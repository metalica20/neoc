# Generated by Django 2.1.5 on 2019-03-06 17:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0004_layertable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layertable',
            name='hazard',
            field=models.CharField(choices=[('flood', 'Flood'), ('landslide', 'Landslide'), ('fire', 'Fire'), ('earthquake', 'Earthquake'), ('light', 'Lightening'), ('lights', 'Lightenings')], max_length=35),
        ),
        migrations.AlterField(
            model_name='school',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=32140),
        ),
    ]
