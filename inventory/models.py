from django.db import models
from bipad.models import TimeStampedModal
from resources.models import Resource


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Item(models.Model):
    KG = 'kg'
    LITRE = 'litre'
    METER_SQUARE = 'm2'
    PCS = 'pcs'
    CARTOON = 'carton'

    UNITS = (
        (KG, 'KG'),
        (LITRE, 'Litre'),
        (METER_SQUARE, 'm2'),
        (PCS, 'PCS'),
        (CARTOON, 'Carton'),
    )
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=25, choices=UNITS)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )

    def __str__(self):
        return '{} ({})'.format(self.title, self.unit)


class Inventory(TimeStampedModal):

    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    resource = models.ForeignKey(
        Resource,
        related_name='inventories',
        on_delete=models.CASCADE
    )
    description = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name_plural = "inventories"
