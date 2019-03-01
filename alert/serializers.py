from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from event.serializers import EventSerializer
from .models import Alert


class AlertSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Alert
        exclude = ('modified_on',)

    expandable_fields = {
        'event': (EventSerializer, {'source': 'event'})
    }
