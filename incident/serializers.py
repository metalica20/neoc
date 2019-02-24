from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from loss.serializers import SimpleLossSerializer
from event.serializers import EventSerializer
from hazard.serializers import HazardSerializer
from federal.serializers import WardSerializer
from .models import Incident


class IncidentSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Incident
        exclude = ('modified_on',)

    expandable_fields = {
        'event': (EventSerializer, {'source': 'event'}),
        'hazard': (HazardSerializer, {'source': 'hazard'}),
        'wards': (WardSerializer, {'source': 'wards'}),
        'loss': (SimpleLossSerializer, {'source': 'loss'}),
    }
