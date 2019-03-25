from django.utils import timezone
from django.contrib.gis.db import models
from bipad.models import TimeStampedModal
from hazard.models import Hazard
from event.models import Event
from federal.models import Ward
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    started_on = models.DateTimeField(blank=True, default=timezone.now)
    expire_on = models.DateTimeField(null=True, blank=True, default=None)
    event = models.ForeignKey(
        Event,
        related_name='alerts',
        on_delete=models.SET_NULL,
        default=None, null=True, blank=True
    )
    wards = models.ManyToManyField(
        Ward,
        blank=True,
        related_name='alerts',
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


@receiver(post_save, sender=Alert)
def on_alert_save(sender, instance, **kwargs):
    if instance.polygon:
        wards = Ward.objects.filter(boundary__intersects=instance.polygon)
        instance.wards.set(wards)
