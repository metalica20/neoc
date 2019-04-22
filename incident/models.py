from django.contrib.gis.db import models
from bipad.models import TimeStampedModal
from loss.models import Loss
from hazard.models import Hazard
from event.models import Event
from federal.models import Ward
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class IncidentSource(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name


class Incident(TimeStampedModal):

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(null=True, blank=True, default=None,
                                   verbose_name=_('Description'))
    cause = models.TextField(
        null=True, blank=True, default=None,
        verbose_name=_('Cause')
    )
    source = models.ForeignKey(
        IncidentSource,
        on_delete=models.PROTECT,
        verbose_name=_('Source')
    )
    verified = models.BooleanField(default=False, verbose_name=_('Verified'))
    approved = models.BooleanField(default=False, verbose_name=_('Approved'))
    # TODO: discuss polygon or multipolygon or simply geometry
    point = models.PointField(
        null=True, blank=True, default=None,
        verbose_name=_('Point')
    )
    polygon = models.MultiPolygonField(
        null=True, blank=True, default=None,
        verbose_name=_('Polygon')
    )
    incident_on = models.DateTimeField(verbose_name=_('Incident On'))
    reported_on = models.DateTimeField(
        null=True, blank=True, default=None,
        verbose_name=_('Reported On')
    )
    event = models.ForeignKey(
        Event,
        related_name='incidents',
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
        verbose_name=_('Event'),
    )
    hazard = models.ForeignKey(
        Hazard,
        related_name='incidents',
        on_delete=models.CASCADE,
        verbose_name=_('Hazard'),
    )
    loss = models.OneToOneField(
        Loss,
        related_name='incident',
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
        verbose_name=_('Loss'),
    )
    wards = models.ManyToManyField(
        Ward,
        blank=True,
        related_name='incidents',
        verbose_name=_('Wards'),
    )
    street_address = models.CharField(
        max_length=255, null=True, blank=True, default=None,
        verbose_name=_('Street Address')
    )
    old = models.BooleanField(default=False, editable=False)
    detail = JSONField(null=True, blank=True, default=None)
    created_by = models.ForeignKey(
        User,
        editable=False,
        related_name='incidents_created',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None
    )
    updated_by = models.ForeignKey(
        User,
        editable=False,
        related_name='incidents_updated',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None
    )

    def __str__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return 'title',

    class Meta:
        permissions = [
            ('can_verify', 'Can verify incident'),
            ('can_approve', 'Can approve incident'),
            ('can_edit', 'Can edit incident'),
        ]
        verbose_name = _('Incident')
        verbose_name_plural = _('Incidents')


class Document(TimeStampedModal):
    incident = models.ForeignKey(
        Incident,
        related_name='incident',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        max_length=255,
        blank=True, null=True, default=None,
        verbose_name=_('Title')
    )
    file = models.FileField(verbose_name=_('Files'), blank=True)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
