# Generated by Django 2.1.5 on 2019-06-05 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0067_auto_20190605_0945'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocioEconomicGapanapa',
            new_name='MunicipalityLevelVulnerability',
        ),
    ]