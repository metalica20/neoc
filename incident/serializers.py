from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from loss.serializers import LossSerializer
from event.serializers import EventSerializer
from hazard.serializers import HazardSerializer
from federal.serializers import WardSerializer
from .models import Incident


class IncidentSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Incident
        exclude = ('modified_on', 'old', 'approved')  # TODO: decide on fields

    expandable_fields = {
        'event': (EventSerializer, {'source': 'event'}),
        'hazard': (HazardSerializer, {'source': 'hazard'}),
        'wards': (WardSerializer, {'source': 'wards', 'many': True}),
        'loss': (LossSerializer, {'source': 'loss'}),
    }
