# Generated by Django 2.1.5 on 2019-03-07 09:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0011_auto_20190307_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('lat', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('long', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326)),
            ],
        ),
    ]
