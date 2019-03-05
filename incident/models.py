from django.contrib.gis.db import models
from bipad.models import TimeStampedModal
from loss.models import Loss
from hazard.models import Hazard
from event.models import Event
from federal.models import Ward
from django.contrib.postgres.fields import JSONField


class IncidentSource(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name


class Incident(TimeStampedModal):
    ARTIFICIAL = 'artificial'
    NATURAL = 'natural'

    INDUCERS = (
        (ARTIFICIAL, 'Artificial'),
        (NATURAL, 'Natural'),
    )

    MINOR = 'minor'
    MAJOR = 'major'
    CATASTROPHIC = 'catastrophic'

    SEVERITY = (
        (MINOR, 'Minor'),
        (MAJOR, 'Major'),
        (CATASTROPHIC, 'catastrophic'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    cause = models.TextField(null=True, blank=True, default=None)
    inducer = models.CharField(
        max_length=25, choices=INDUCERS,
        null=True, blank=True, default=None
    )
    severity = models.CharField(
        max_length=25, choices=SEVERITY,
        null=True, blank=True, default=None
    )
    source = models.ForeignKey(IncidentSource, on_delete=models.PROTECT)
    verified = models.BooleanField(default=False)
    # TODO: discuss polygon or multipolygon or simply geometry
    point = models.PointField(null=True, blank=True, default=None)
    polygon = models.MultiPolygonField(null=True, blank=True, default=None)
    incident_on = models.DateTimeField(null=True, blank=True, default=None)
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    hazard = models.ForeignKey(
        Hazard,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    loss = models.OneToOneField(
        Loss,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    wards = models.ManyToManyField(
        Ward,
        related_name='incidents',
    )
    street_address = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    detail = JSONField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title
