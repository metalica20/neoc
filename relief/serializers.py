from rest_framework import serializers
from .models import (
    Release,
    Flow,
)


class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        exclude = ('modified_on',)


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        exclude = ('modified_on',)
