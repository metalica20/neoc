# Generated by Django 2.1.5 on 2019-04-11 05:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_polygon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, default=None, null=True, srid=4326, verbose_name='Polygon'),
        ),
        migrations.AlterField(
            model_name='event',
            name='severity',
            field=models.CharField(blank=True, choices=[('minor', 'Minor'), ('major', 'Major'), ('catastrophic', 'Catastrophic')], default=None, max_length=25, null=True, verbose_name='Severity'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
