# Generated by Django 2.1.5 on 2019-06-05 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0068_auto_20190605_1017'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Risk',
            new_name='DistrictLevelVulnerability',
        ),
    ]