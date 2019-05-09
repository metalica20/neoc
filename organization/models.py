from django.db import models
from federal.models import Ward


class Responsibility(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Organization(models.Model):
    title = models.CharField(max_length=255)
    responsible_for = models.ManyToManyField(
        Responsibility,
        related_name="organizations"
    )
    short_name = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    long_name = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    wards = models.ManyToManyField(Ward, related_name='organizations')

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(
        Organization,
        related_name='projects',
        on_delete=models.CASCADE
    )
    wards = models.ManyToManyField(Ward, related_name='projects')

    def __str__(self):
        return self.title
