from rest_framework import serializers
from loss.serializers import SimpleLossSerializer
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    loss = SimpleLossSerializer(read_only=True)

    class Meta:
        model = Incident
        exclude = ('modified_on',)
