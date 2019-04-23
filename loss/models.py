from django.db import models
from django.contrib.postgres.fields import JSONField
from bipad.models import TimeStampedModal, DistinctSum
from django.db.models import Q
from django.db.models.functions import Coalesce
from resources.models import Resource
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from federal.models import Ward


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
    description = models.TextField(null=True, blank=True, default=None,
                                   verbose_name=_('Description'))
    estimated_loss = models.BigIntegerField(
        null=True, blank=True, default=None,
        verbose_name=_('Estimated Loss')
    )
    detail = JSONField(null=True, blank=True, default=None,)

    objects = models.Manager()
    with_stat = StatManager()

    def __str__(self):
        from incident.models import Incident
        return str(Incident.objects.filter(loss=self).first())

    @staticmethod
    def autocomplete_search_fields():
        return 'incident__title',

    class Meta:
        verbose_name = _('Loss')
        verbose_name_plural = _("Losses")


class DisabilityType(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'country'
        verbose_name_plural = "countries"


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
        (DEAD, _('Dead')),
        (MISSING, _('Missing')),
        (INJURED, _('Injured')),
        (AFFECTED, _('Affected')),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHERS = 'others'

    GENDERS = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (OTHERS, _('Others')),
    )

    status = models.CharField(max_length=25, choices=STATUS, verbose_name=_('Status'))
    name = models.CharField(
        max_length=255,
        null=True, blank=True, default=None,
        verbose_name=_('Name'),
    )
    age = models.PositiveSmallIntegerField(
        null=True, blank=True, default=None, verbose_name=_('Age'),)
    gender = models.CharField(
        max_length=25,
        null=True, blank=True, default=None,
        choices=GENDERS,
        verbose_name=_('Gender'),
    )
    nationality = models.ForeignKey(
        Country,
        related_name="peoples",
        null=True, blank=True, default=None,
        on_delete=models.PROTECT,
        verbose_name=_('Nationality')
    )
    ward = models.ForeignKey(
        Ward,
        blank=True, null=True, default=None,
        related_name='peoples',
        verbose_name=_('Ward'),
        on_delete=models.CASCADE
    )
    below_poverty = models.BooleanField(
        null=True, blank=True, default=None,
        verbose_name=_('Below Poverty')
    )
    disability = models.ForeignKey(
        DisabilityType,
        related_name="peoples",
        null=True, blank=True, default=None,
        on_delete=models.PROTECT,
        verbose_name=_('Disability')
    )
    count = models.PositiveIntegerField(default=1, verbose_name=_('Count'))
    loss = models.ForeignKey(
        Loss, related_name='peoples', on_delete=models.PROTECT)

    def __str__(self):
        return self.name or 'People-{}'.format(self.id)

    class Meta:
        verbose_name = _('People')
        verbose_name_plural = _('People')


class Family(TimeStampedModal):
    """
    Family

    Can be single with count 1 or bulk
    """
    AFFECTED = 'affected'
    RELOCATED = 'relocated'
    EVACUATED = 'evacuated'

    STATUS = (
        (AFFECTED, _('Affected')),
        (RELOCATED, _('Relocated')),
        (EVACUATED, _('Evacuated')),
    )

    title = models.CharField(max_length=255, null=True,
                             blank=True, default=None, verbose_name=_('Owner Name'))
    ward = models.ForeignKey(
        Ward,
        blank=True, null=True, default=None,
        related_name='families',
        verbose_name=_('Ward'),
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=25, choices=STATUS, verbose_name=_('Status'))
    below_poverty = models.BooleanField(
        null=True, blank=True, default=None, verbose_name=_('Below Poverty'))
    count = models.PositiveIntegerField(default=1, verbose_name=_('Count'))
    phone_number = models.CharField(
        max_length=25, null=True, blank=True, default=None,
        verbose_name=_('Phone Number')
    )
    loss = models.ForeignKey(
        Loss, related_name='families', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = _('Families')
        verbose_name = _('Family')


class InfrastructureType(MPTTModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(
        max_length=255,
        null=True, blank=True, default=None
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True, blank=True, default=None,
        related_name='children'
    )
    # TODO: can also relate to resource_type

    def __str__(self):
        return self.title


class InfrastructureUnit(models.Model):
    title = models.CharField(max_length=255, unique=True)

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
        (DESTROYED, _('Destroyed')),
        (AFFECTED, _('Affected')),
    )

    title = models.CharField(max_length=255, null=True,
                             blank=True, default=None,
                             verbose_name=_('Infrastructure Title'))
    type = models.ForeignKey(
        InfrastructureType,
        related_name='infrastructures',
        on_delete=models.PROTECT,
        verbose_name=_('Type')
    )

    status = models.CharField(max_length=25, choices=STATUS, verbose_name=_('Status'))
    resource = models.ForeignKey(
        Resource,
        null=True, blank=True, default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('Resource')
    )
    equipment_value = models.PositiveIntegerField(
        null=True, blank=True, default=None,
        verbose_name=_('Equipment Value')
    )
    infrastructure_value = models.PositiveIntegerField(
        null=True, blank=True, default=None,
        verbose_name=_('Infrastructure Value')
    )
    unit = models.ForeignKey(
        InfrastructureUnit,
        blank=True, default=None, null=True,
        on_delete=models.PROTECT,
        verbose_name=_('Unit')
    )
    beneficiary_owner = models.CharField(
        max_length=255, null=True, blank=True, default=None,
        verbose_name=_('Beneficiary Owner')
    )
    beneficiary_count = models.PositiveIntegerField(
        null=True, blank=True, default=None,
        verbose_name=_('Beneficiary Count')
    )
    service_disrupted = models.BooleanField(
        max_length=255,
        null=True, blank=True, default=None,
        verbose_name=_('Service Disrupted')
    )
    count = models.PositiveIntegerField(default=1, verbose_name=_('Count'))
    economic_loss = models.BigIntegerField(
        null=True, blank=True, default=None,
        verbose_name=_('Economic Loss')
    )
    loss = models.ForeignKey(
        Loss, related_name='infrastructures', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Infrastructure')
        verbose_name_plural = _('Infrastructures')


class LivestockType(MPTTModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(
        max_length=255,
        null=True, blank=True, default=None
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True, blank=True, default=None,
        related_name='children'
    )

    def __str__(self):
        return self.title


class Livestock(TimeStampedModal):
    DESTROYED = 'destroyed'
    AFFECTED = 'affected'

    STATUS = (
        (DESTROYED, _('Destroyed')),
        (AFFECTED, _('Affected')),
    )

    title = models.CharField(
        max_length=255,
        null=True, blank=True, default=None,
        verbose_name=_('Title')
    )
    type = models.ForeignKey(
        LivestockType,
        related_name='livestocks',
        on_delete=models.PROTECT,
        verbose_name=_('Type')
    )
    status = models.CharField(max_length=25, choices=STATUS, verbose_name=_('Status'))
    count = models.PositiveIntegerField(verbose_name=_('Count'))
    economic_loss = models.BigIntegerField(
        null=True, blank=True, default=None,
        verbose_name=_('Economic Loss')
    )
    loss = models.ForeignKey(
        Loss, related_name='livestocks', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Livestock')
        verbose_name_plural = _('Livestocks')


class AgricultureType(MPTTModel):
    title = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None,
        related_name='children'
    )

    def __str__(self):
        return '{} ({})'.format(self.title, self.unit)


class Agriculture(TimeStampedModal):
    type = models.ForeignKey(
        AgricultureType,
        related_name='agricultures',
        on_delete=models.PROTECT,
        verbose_name=_('Type')
    )
    beneficiary_owner = models.CharField(
        max_length=255,
        null=True, blank=True, default=None,
        verbose_name=_('Beneficiary Owner')
    )
    beneficiary_count = models.PositiveIntegerField(
        default=None, null=True, blank=True,
        verbose_name=_('Beneficiary Count')
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('Quantity')
    )
    loss = models.ForeignKey(
        Loss, related_name='agricultures', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Agriculture')
        verbose_name_plural = _('Agriculture')
