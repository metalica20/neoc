# Generated by Django 2.1.5 on 2019-05-21 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0050_flood_basin_flood_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flood_basin',
            new_name='FloodBasin',
        ),
        migrations.RenameModel(
            old_name='Flood_time',
            new_name='FloodPeriod',
        ),
    ]