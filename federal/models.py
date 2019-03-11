from django.contrib.gis.db import models


class Province(models.Model):
    title = models.CharField(max_length=25)
    boundary = models.MultiPolygonField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=25)
    boundary = models.MultiPolygonField(null=True, blank=True, default=None)
    province = models.ForeignKey(
        Province,
        related_name='districts',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title


class Municipality(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, null=True, blank=True, default=None)
    boundary = models.MultiPolygonField(null=True, blank=True, default=None)
    district = models.ForeignKey(
        District,
        related_name='municipalities',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'{self.title} {self.type}'

    class Meta:
        verbose_name_plural = "municipalities"


class Ward(models.Model):
    title = models.CharField(max_length=25)
    boundary = models.MultiPolygonField(null=True, blank=True, default=None)
    municipality = models.ForeignKey(
        Municipality,
        related_name='wards',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'{str(self.municipality)}-{self.title}'
