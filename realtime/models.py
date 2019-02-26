from django.contrib.gis.db import models
from bipad.models import TimeStampedModal
from django.contrib.postgres.fields import JSONField


class Earthquake(TimeStampedModal):
    description = models.TextField(default=None, null=True, blank=True)
    point = models.PointField()
    magnitude = models.FloatField()
    address = models.CharField(max_length=255, null=True, blank=True)
    event_on = models.DateTimeField()


class River(TimeStampedModal):
    id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    basin = models.CharField(max_length=255)
    point = models.PointField(null=True, blank=True)
    water_level_value = models.FloatField(null=True, blank=True)
    water_level_datetime = models.DateTimeField(null=True, blank=True)
    danger_level = models.FloatField(null=True, blank=True)
    warning_level = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=25,null=True, blank=True)
    elevation = models.IntegerField(null=True, blank=True)
    steady = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    station_series_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Rain(TimeStampedModal):
    id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    basin = models.CharField(max_length=255)
    point = models.PointField(null=True, blank=True)
    elevation = models.IntegerField(null=True, blank=True)
    averages = JSONField()
    status = models.CharField(max_length=25,null=True, blank=True)
    district = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    station_series_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
