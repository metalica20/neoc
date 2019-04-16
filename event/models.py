from django.utils import timezone
from django.contrib.gis.db import models
from bipad.models import TimeStampedModal
from django.utils.translation import ugettext_lazy as _


class Event(TimeStampedModal):
    MINOR = 'minor'
    MAJOR = 'major'
    CATASTROPHIC = 'catastrophic'

    SEVERITY = (
        (MINOR, _('Minor')),
        (MAJOR, _('Major')),
        (CATASTROPHIC, _('Catastrophic')),
    )

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(
        null=True, blank=True, default=None,
        verbose_name=_('Description'),
    )
    point = models.PointField(
        null=True, blank=True, default=None,
        verbose_name=_('Point')
    )
    polygon = models.PolygonField(
        null=True, blank=True, default=None,
        verbose_name=_('Polygon')
    )
    started_on = models.DateTimeField(
        blank=True,
        default=timezone.now,
        verbose_name=_('Started on')
    )
    ended_on = models.DateTimeField(
        null=True, blank=True, default=None,
        verbose_name=_('Ended on')
    )
    severity = models.CharField(
        max_length=25,
        choices=SEVERITY,
        null=True, blank=True, default=None,
        verbose_name=_('Severity'),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
