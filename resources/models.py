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
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    detail = JSONField(null=True, blank=True, default=None)

    @staticmethod
    def autocomplete_search_fields():
        return 'title',

    def __str__(self):
        return self.title


class Education(Resource):
    classroom_count = models.PositiveIntegerField(null=True, blank=True, default=None)
    operator_type = models.CharField(max_length=255, null=True, blank=True, default=None)
    opening_hours = models.CharField(max_length=255, null=True, blank=True, default=None)
    phone_number = models.CharField(max_length=255, null=True, blank=True, default=None)
    email_address = models.EmailField(null=True, blank=True, default=None)
    no_of_employee = models.PositiveIntegerField(null=True, blank=True, default=None)
    no_of_student = models.PositiveIntegerField(null=True, blank=True, default=None)
    type = models.CharField(max_length=255, null=True, blank=True, default=None)


class Health(Resource):
    bed_count = models.PositiveIntegerField(null=True, blank=True, default=None)
    type = models.CharField(max_length=255, null=True, blank=True, default=None)
    cbs_code = models.IntegerField(null=True, blank=True, default=None)
    phone_number = models.CharField(max_length=255, null=True, blank=True, default=None)
    email_address = models.EmailField(null=True, blank=True, default=None)
    emergency_service = models.BooleanField(null=True, blank=True, default=None)
    icu = models.BooleanField(null=True, blank=True, default=None)
    nicu = models.BooleanField(null=True, blank=True, default=None)
    operating_theater = models.BooleanField(null=True, blank=True, default=None)
    x_ray = models.BooleanField(null=True, blank=True, default=None)
    ambulance_service = models.BooleanField(null=True, blank=True, default=None)
    opening_hours = models.CharField(max_length=255, null=True, blank=True, default=None)
    operator_type = models.CharField(max_length=255, null=True, blank=True, default=None)
    no_of_staffs = models.PositiveIntegerField(null=True, blank=True, default=None)


class Finance(Resource):

    BLB = 'blb'
    BRANCH = 'branch'
    ATM = 'atm'

    CHANNELS = (
        (BLB, 'Branchless Banking'),
        (BRANCH, 'Branch'),
        (ATM, 'ATM'),
    )
    MONEY_EXCHANGE = 'bureau_de_change'
    BANK = 'bank'
    ATM = 'atm'

    TYPES = (
        (MONEY_EXCHANGE, 'Money Exchange'),
        (BANK, 'Bank'),
        (ATM, 'ATM'),
    )

    cbs_code = models.IntegerField(null=True, blank=True, default=None)
    population = models.PositiveIntegerField(null=True, blank=True, default=None)
    channel = models.CharField(null=True, blank=True, default=None, max_length=25, choices=CHANNELS)
    access_point_count = models.PositiveIntegerField(default=1)
    type = models.CharField(null=True, blank=True, default=None, max_length=25, choices=TYPES)
    phone_number = models.CharField(max_length=255, null=True, blank=True, default=None)
    email_address = models.EmailField(null=True, blank=True, default=None)
    website = models.CharField(max_length=255, null=True, blank=True, default=None)
    opening_hours = models.CharField(max_length=255, null=True, blank=True, default=None)
    operator_type = models.CharField(max_length=255, null=True, blank=True, default=None)
    bank_type = models.CharField(max_length=255, null=True, blank=True, default=None)
    atm_available = models.BooleanField(null=True, blank=True, default=None)
    place_address = models.CharField(max_length=255, null=True, blank=True, default=None)
    network = models.CharField(max_length=255, null=True, blank=True, default=None)


class Communication(Resource):
    pass


class Governance(Resource):
    POLICE = 'police'
    TYPES = (
        (POLICE, 'Police'),
    )
    type = models.CharField(null=True, blank=True, default=None, max_length=25, choices=TYPES)
    phone_number = models.CharField(max_length=255, null=True, blank=True, default=None)
    email_address = models.EmailField(null=True, blank=True, default=None)
    website = models.CharField(max_length=255, null=True, blank=True, default=None)


class Tourism(Resource):
    pass


class Cultural(Resource):
    religion = models.CharField(max_length=25, null=True, blank=True, default=None)
    phone_number = models.CharField(max_length=255, null=True, blank=True, default=None)
    opening_hours = models.CharField(max_length=255, null=True, blank=True, default=None)


class Industry(Resource):
    pass
