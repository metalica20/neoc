from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        exclude = ('modified_on',)
