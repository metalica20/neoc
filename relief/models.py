from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from bipad.models import TimeStampedModal
from organization.models import Organization
from event.models import Event
from incident.models import Incident
from loss.models import People
from federal.models import Ward


class FiscalYear(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Flow(TimeStampedModal):
    INFLOW = 'inflow'
    INITIAL_BALANCE = 'initial balance'

    TYPES = (
        (INFLOW, 'Inflow'),
        (INITIAL_BALANCE, 'Initial Balance'),
    )

    receiver_organization = models.ForeignKey(
        Organization,
        related_name='received_flows',
        on_delete=models.CASCADE,
    )
    provider_organization = models.ForeignKey(
        Organization,
        related_name='provided_flows',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None,
    )
    event = models.ForeignKey(
        Event,
        related_name='flows',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None,
    )
    type = models.CharField(max_length=25, choices=TYPES)
    amount = models.BigIntegerField()
    fiscal_year = models.ForeignKey(
        FiscalYear,
        on_delete=models.SET_NULL,
        related_name='flows',
        null=True, blank=False, default=None,
    )
    date = models.DateField(
        blank=True,
        default=timezone.now,
    )
    description = models.TextField(null=True, blank=True, default=None)

    def clean(self):
        if self.type == 'inflow' and self.provider_organization is None:
            raise ValidationError(_('Provider organization cannot be empty when type is inflow.'))


class ReleaseStatus(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ReleaseStatus"


class Release(TimeStampedModal):
    provider_organization = models.ForeignKey(
        Organization,
        related_name='provided_realeases',
        on_delete=models.CASCADE,
    )
    incident = models.ForeignKey(
        Incident,
        related_name='realeases',
        on_delete=models.CASCADE,
    )
    ward = models.ForeignKey(
        Ward,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
    )
    person = models.ForeignKey(
        People,
        related_name='realeases',
        on_delete=models.CASCADE,
    )
    beneficiary = models.ForeignKey(
        People,
        related_name='beneficiary_releases',
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
    )
    beneficiary_other = models.CharField(
        max_length=25,
        null=True, blank=True, default=None,
    )
    status = models.ForeignKey(
        ReleaseStatus,
        related_name='releases',
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
    )
    amount = models.BigIntegerField()
    description = models.TextField(null=True, blank=True, default=None)
