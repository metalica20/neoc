from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType


class Hazard(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(default=None, null=True, blank=True)
    icon = models.CharField(max_length=25, default=None, null=True, blank=True)
    resources = models.ManyToManyField(ContentType, through="HazardResources")

    def __str__(self):
        return self.title


class HazardResources(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE)
    resource = models.ForeignKey(
        ContentType,
        limit_choices_to=Q(app_label='resources') & ~Q(model='resource'),
        on_delete=models.CASCADE
    )
    weight = models.IntegerField(default=0)
