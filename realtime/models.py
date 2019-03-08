from django.contrib.gis.db import models
from bipad.models import TimeStampedModal
from django.contrib.postgres.fields import JSONField


class Earthquake(TimeStampedModal):
    description = models.TextField(null=True, blank=True, default=None)
    point = models.PointField()
    magnitude = models.FloatField()
    address = models.CharField(max_length=255, null=True, blank=True, default=None)
    event_on = models.DateTimeField()


class River(TimeStampedModal):
    title = models.CharField(max_length=255)
    basin = models.CharField(max_length=255)
    point = models.PointField(null=True, blank=True, default=None)
    water_level = models.FloatField(null=True, blank=True, default=None)
    danger_level = models.FloatField(null=True, blank=True, default=None)
    warning_level = models.FloatField(null=True, blank=True, default=None)
    water_level_on = models.DateTimeField(null=True, blank=True, default=None)
    status = models.CharField(max_length=25, null=True, blank=True, default=None)
    elevation = models.IntegerField(null=True, blank=True, default=None)
    steady = models.CharField(max_length=25, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    station_series_id = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class Rain(TimeStampedModal):
    title = models.CharField(max_length=255)
    basin = models.CharField(max_length=255)
    point = models.PointField(null=True, blank=True, default=None)
    elevation = models.IntegerField(null=True, blank=True, default=None)
    averages = JSONField()
    status = models.CharField(max_length=25, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    station_series_id = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title
