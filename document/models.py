from django.db import models
from bipad.models import TimeStampedModal
from event.models import Event
from federal.models import(
    Province,
    District,
    Municipality,
)
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Document(TimeStampedModal):
    MUNICIPALITY = 'municipality'
    DISTRICT = 'district'
    PROVINCE = 'province'
    NATIONAL = 'national'

    REGIONS = (
        (MUNICIPALITY, 'Municipality'),
        (DISTRICT, 'District'),
        (PROVINCE, 'Province'),
        (NATIONAL, 'National'),
    )
    title = models.CharField(max_length=255, null=True, blank=True, default=None)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    region = models.CharField(
        max_length=25,
        blank=True, null=True, default='national',
        choices=REGIONS
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    file = models.FileField()
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    published_date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title

