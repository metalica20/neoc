from rest_framework import serializers
from .models import Hazard


class HazardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hazard
        exclude = ('resources', 'order')
