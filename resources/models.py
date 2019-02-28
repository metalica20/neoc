from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from polymorphic.models import PolymorphicModel
from federal.models import Ward


class Resource(PolymorphicModel):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    point = models.PointField(null=True, blank=True, default=None)
    ward = models.ForeignKey(
        Ward,
        related_name='resources',
        on_delete=models.PROTECT,
    )

    detail = JSONField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class Education(Resource):
    classroom_count = models.PositiveIntegerField()


class Health(Resource):
    bed_count = models.PositiveIntegerField()


class Finance(Resource):

    BLB = 'blb'
    BRANCH = 'branch'
    ATM = 'atm'

    CHANNELS = (
        (BLB, 'Branchless Banking'),
        (BRANCH, 'Branch'),
        (ATM, 'ATM'),
    )
    cbs_code = models.IntegerField(null=True, blank=True, default=None)
    channel = models.CharField(max_length=25, choices=CHANNELS)
    population = models.PositiveIntegerField()
    access_point_count = models.PositiveIntegerField(default=1)


class Communication(Resource):
    pass


class Governance(Resource):
    pass


class Tourism(Resource):
    pass


class Industry(Resource):
    pass
