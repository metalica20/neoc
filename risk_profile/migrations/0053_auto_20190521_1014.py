# Generated by Django 2.1.5 on 2019-05-21 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0052_floodperioddetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floodperiod',
            name='floodBasin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FloodPeriod', to='risk_profile.FloodBasin'),
        ),
    ]