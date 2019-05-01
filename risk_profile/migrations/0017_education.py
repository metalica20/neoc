# Generated by Django 2.1.5 on 2019-03-07 16:56

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0016_auto_20190307_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('lat', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('long', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326)),
            ],
        ),
    ]