# Generated by Django 2.1.5 on 2019-04-04 02:19

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, default=None, null=True, srid=4326),
        ),
    ]