from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from .models import Event


class EventSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('modified_on',)
