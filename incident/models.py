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
    NON_NATURAL = 'non_natural'
    NATURAL = 'natural'

    INDUCERS = (
        (NON_NATURAL, 'Non Natural'),
        (NATURAL, 'Natural'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    cause = models.TextField(null=True, blank=True, default=None)
    inducer = models.CharField(
        max_length=25, choices=INDUCERS,
        null=True, blank=True, default=None
    )
    source = models.ForeignKey(IncidentSource, on_delete=models.PROTECT)
    verified = models.BooleanField(default=False)
    # TODO: discuss polygon or multipolygon or simply geometry
    point = models.PointField(null=True, blank=True, default=None)
    polygon = models.MultiPolygonField(null=True, blank=True, default=None)
    incident_on = models.DateTimeField(null=True, blank=True, default=None)
    reported_on = models.DateTimeField(null=True, blank=True, default=None)
    event = models.ForeignKey(
        Event,
        related_name='incidents',
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    hazard = models.ForeignKey(
        Hazard,
        related_name='incidents',
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    loss = models.OneToOneField(
        Loss,
        related_name='incident',
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    wards = models.ManyToManyField(
        Ward,
        blank=True,
        related_name='incidents',
    )
    street_address = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    old = models.BooleanField(default=False, editable=False)
    detail = JSONField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ('can_verify', 'Can verify incident'),
        ]


class Document(TimeStampedModal):
    incident = models.ForeignKey(
        Incident, related_name='incident', on_delete=models.PROTECT)
    title = models.CharField(max_length=255, blank=True, null=True, default=None)
    file = models.FileField(verbose_name='files', blank=True,)
