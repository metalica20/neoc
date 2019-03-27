from django.db import models
from django.contrib.postgres.fields import JSONField
from bipad.models import TimeStampedModal, DistinctSum
from django.db.models import Q
from django.db.models.functions import Coalesce


class StatManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            people_death_count=Coalesce(DistinctSum(
                'peoples__count',
                filter=Q(peoples__status='dead')
            ), 0),
            livestock_destroyed_count=Coalesce(DistinctSum(
                'livestocks__count',
                filter=Q(livestocks__status='destroyed')
            ), 0),
            infrastructure_destroyed_count=Coalesce(DistinctSum(
                'infrastructures__count',
                filter=Q(infrastructures__status='destroyed')
            ), 0),
        )


class Loss(TimeStampedModal):
    """
    Loss

    Allows to accomodate both historical data with less details and
    current Nepal Police and other data with finer details
    """
    description = models.TextField(null=True, blank=True, default=None)
    estimated_loss = models.BigIntegerField(
        null=True, blank=True, default=None
    )
    detail = JSONField(null=True, blank=True, default=None)

    objects = models.Manager()
    with_stat = StatManager()

    def __str__(self):
        from incident.models import Incident
        return str(Incident.objects.filter(loss=self).first())

    @staticmethod
    def autocomplete_search_fields():
        return 'incident__title',

    class Meta:
        verbose_name_plural = "losses"


class People(TimeStampedModal):
    """
    People

    Can be single with count 1 or bulk
    """
    DEAD = 'dead'
    MISSING = 'missing'
    INJURED = 'injured'
    AFFECTED = 'affected'

    STATUS = (
        (DEAD, 'Dead'),
        (MISSING, 'Missing'),
        (INJURED, 'Injured'),
        (AFFECTED, 'Affected'),
    )

    MALE = 'male'
    FEMALE = 'female'

    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    status = models.CharField(max_length=25, choices=STATUS)
    name = models.CharField(
        max_length=255,
        null=True, blank=True, default=None
    )
    age = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    gender = models.CharField(
        max_length=25,
        null=True, blank=True, default=None,
        choices=GENDERS
    )
    below_poverty = models.BooleanField(null=True, blank=True, default=None)
    disabled = models.BooleanField(null=True, blank=True, default=None)
    count = models.PositiveIntegerField(default=1)
    loss = models.ForeignKey(
        Loss, related_name='peoples', on_delete=models.CASCADE)


class Family(TimeStampedModal):
    """
    Family

    Can be single with count 1 or bulk
    """
    AFFECTED = 'affected'
    RELOCATED = 'relocated'
    EVACUATED = 'evacuated'

    STATUS = (
        (AFFECTED, 'Affected'),
        (RELOCATED, 'Relocated'),
        (EVACUATED, 'Evacuated'),
    )

    title = models.CharField(max_length=255, null=True,
                             blank=True, default=None)
    status = models.CharField(max_length=25, choices=STATUS)
    below_poverty = models.BooleanField(null=True, blank=True, default=None)
    count = models.PositiveIntegerField(default=1)
    phone_number = models.CharField(
        max_length=25, null=True, blank=True, default=None
    )
    loss = models.ForeignKey(
        Loss, related_name='families', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "families"


class InfrastructureType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    # TODO: can also relate to resource_type

    def __str__(self):
        return self.title


class Infrastructure(TimeStampedModal):
    """
    Insfrastructure

    Can be single with count 1 or bulk
    """
    DESTROYED = 'destroyed'
    AFFECTED = 'affected'

    STATUS = (
        (DESTROYED, 'Destroyed'),
        (AFFECTED, 'Affected'),
    )

    title = models.CharField(max_length=255, null=True,
                             blank=True, default=None)
    type = models.ForeignKey(
        InfrastructureType, related_name='infrastructures', on_delete=models.PROTECT)
    status = models.CharField(max_length=25, choices=STATUS)
    equipment_value = models.PositiveIntegerField(
        null=True, blank=True, default=None
    )
    infrastructure_value = models.PositiveIntegerField(
        null=True, blank=True, default=None
    )
    beneficiary_owner = models.CharField(
        max_length=255, null=True, blank=True, default=None
    )
    service_disrupted = models.BooleanField(
        max_length=255, null=True, blank=True, default=None
    )
    count = models.PositiveIntegerField(default=1)
    economic_loss = models.BigIntegerField(
        null=True, blank=True, default=None
    )
    loss = models.ForeignKey(
        Loss, related_name='infrastructures', on_delete=models.CASCADE
    )


class LivestockType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(
        max_length=255, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.title


class Livestock(TimeStampedModal):
    DESTROYED = 'destroyed'
    AFFECTED = 'affected'

    STATUS = (
        (DESTROYED, 'Destroyed'),
        (AFFECTED, 'Affected'),
    )

    title = models.CharField(
        max_length=255,
        null=True, blank=True, default=None
    )
    type = models.ForeignKey(
        LivestockType,
        related_name='livestocks',
        on_delete=models.PROTECT
    )
    status = models.CharField(max_length=25, choices=STATUS)
    count = models.PositiveIntegerField()
    economic_loss = models.BigIntegerField(
        null=True, blank=True, default=None
    )
    loss = models.ForeignKey(
        Loss, related_name='livestocks', on_delete=models.CASCADE
    )
