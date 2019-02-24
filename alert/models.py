from django.contrib.gis.db import models
from bipad.models import TimeStampedModal

from hazard.models import Hazard
from event.models import Event


class Alert(TimeStampedModal):

    DHM = 'dhm'
    OTHERS = 'other'

    SOURCES = (
        (DHM, 'dhm'),
        (OTHERS, 'Other'),
    )

    title = models.CharField(max_length=255)
    source = models.CharField(max_length=255, choices=SOURCES, default=OTHERS)
    description = models.TextField()
    verified = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    hazard = models.ForeignKey(
        Hazard,
        on_delete=models.SET_NULL,
        default=None, null=True, blank=True
    )
    expire_on = models.DateTimeField(null=True, blank=True, default=None)
    event = models.ForeignKey(
        Event,
        related_name='alerts',
        on_delete=models.SET_NULL,
        default=None, null=True, blank=True
    )
    polygon = models.MultiPolygonField(null=True, blank=True, default=None)
    # TODO: discuss location

    def __str__(self):
        return self.title


class Activity(TimeStampedModal):
    SENT = 'sent'
    DELIVERED = 'delivered'
    FAILED = 'failed'

    EMAIL = 'email'
    SMS = 'sms'

    STATUSES = (
        (SENT, 'Sent'),
        (DELIVERED, 'Delivered'),
        (FAILED, 'Failed'),
    )

    TYPES = (
        (EMAIL, 'Email'),
        (SMS, 'SMS'),
    )

    type = models.CharField(
        max_length=25,
        choices=TYPES,
    )
    status = models.CharField(
        max_length=25,
        choices=STATUSES,
    )
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
