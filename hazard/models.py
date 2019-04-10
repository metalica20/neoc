from colorfield.fields import ColorField
from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType


class Hazard(models.Model):
    NON_NATURAL = 'non_natural'
    NATURAL = 'natural'

    TYPES = (
        (NON_NATURAL, 'Non Natural'),
        (NATURAL, 'Natural'),
    )

    title = models.CharField(max_length=250, unique=True)
    order = models.SmallIntegerField(default=None, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    icon = models.CharField(max_length=25, default=None, null=True, blank=True)
    color = ColorField(default=None, null=True, blank=True)
    resources = models.ManyToManyField(ContentType, through="HazardResources")
    type = models.CharField(
        max_length=25, choices=TYPES,
        null=True, blank=True, default=None
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class HazardResources(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE)
    resource = models.ForeignKey(
        ContentType,
        limit_choices_to=Q(app_label='resources') & ~Q(model='resource'),
        on_delete=models.CASCADE
    )
    weight = models.IntegerField(default=0)
