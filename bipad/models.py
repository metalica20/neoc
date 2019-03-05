from django.db import models


class TimeStampedModal(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DistinctSum(models.Sum):
    function = "SUM"
    template = "%(function)s(DISTINCT %(expressions)s)"
