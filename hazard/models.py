from colorfield.fields import ColorField
from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator


class Hazard(models.Model):
    NON_NATURAL = 'non natural'
    NATURAL = 'natural'

    TYPES = (
        (NON_NATURAL, _('Non Natural')),
        (NATURAL, _('Natural')),
    )

    title = models.CharField(max_length=250, unique=True, verbose_name=_('Title'))
    order = models.SmallIntegerField(
        default=None, null=True, blank=True,
        verbose_name=_('Order')
    )
    description = models.TextField(
        default=None, null=True, blank=True,
        verbose_name=_('Description')
    )
    icon = models.FileField(
        upload_to='hazard-icons/',
        default=None, null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['svg'])],
        verbose_name=_('Icon')
    )
    color = ColorField(
        default=None, null=True, blank=True,
        verbose_name=_('Color')
    )
    resources = models.ManyToManyField(
        ContentType,
        through="HazardResources",
        verbose_name=_('Resources')
    )
    type = models.CharField(
        max_length=25, choices=TYPES,
        null=True, blank=True, default=None,
        verbose_name=_('Type')
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
        verbose_name = _('Hazard')
        verbose_name_plural = _('Hazards')


class HazardResources(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE)
    resource = models.ForeignKey(
        ContentType,
        limit_choices_to=Q(app_label='resources') & ~Q(model='resource'),
        on_delete=models.CASCADE
    )
    weight = models.IntegerField(default=0)
