# Generated by Django 2.1.5 on 2019-04-11 05:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0014_remove_incident_inducer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'permissions': [('can_verify', 'Can verify incident'), ('can_approve', 'Can approve incident')], 'verbose_name': 'Incident', 'verbose_name_plural': 'Incidents'},
        ),
        migrations.AlterField(
            model_name='incident',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='cause',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Cause'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='event',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incidents', to='event.Event', verbose_name='Event'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='hazard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to='hazard.Hazard', verbose_name='Hazard'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_on',
            field=models.DateTimeField(verbose_name='Incident On'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='loss',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incident', to='loss.Loss', verbose_name='Loss'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326, verbose_name='Point'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='polygon',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, default=None, null=True, srid=4326, verbose_name='Polygon'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='reported_on',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Reported On'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='incident.IncidentSource', verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='street_address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Street Address'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='Verified'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='wards',
            field=models.ManyToManyField(blank=True, related_name='incidents', to='federal.Ward', verbose_name='Wards'),
        ),
    ]