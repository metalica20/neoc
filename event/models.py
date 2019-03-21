from django.db import models
from bipad.models import TimeStampedModal


class Event(TimeStampedModal):
    MINOR = 'minor'
    MAJOR = 'major'
    CATASTROPHIC = 'catastrophic'

    SEVERITY = (
        (MINOR, 'Minor'),
        (MAJOR, 'Major'),
        (CATASTROPHIC, 'Catastrophic'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)

    severity = models.CharField(
        max_length=25, choices=SEVERITY,
        null=True, blank=True, default=None
    )

    def __str__(self):
        return self.title
