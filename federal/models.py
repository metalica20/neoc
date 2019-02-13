from django.db import models


class Province(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=25)
    province = models.ForeignKey(
        Province,
        related_name='districts',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title


class Municipality(models.Model):
    title = models.CharField(max_length=25)
    district = models.ForeignKey(
        District,
        related_name='municipalities',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "municipalities"


class Ward(models.Model):
    title = models.CharField(max_length=25)
    municipality = models.ForeignKey(
        Municipality,
        related_name='wards',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title
