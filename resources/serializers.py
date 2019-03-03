from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    resource_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='model',
        source='polymorphic_ctype',
    )

    def get_distance(self, obj):
        if obj.distance:
            return int(obj.distance.m)
        return None

    class Meta:
        model = Resource
        fields = (
            'title',
            'description',
            'point',
            'ward',
            'resource_type',
        )


class ResponseSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()
    resource_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='model',
        source='polymorphic_ctype',
    )

    def get_distance(self, obj):
        if obj.distance:
            return int(obj.distance.m) or 0
        return None

    class Meta:
        model = Resource
        fields = (
            'title',
            'description',
            'point',
            'ward',
            'resource_type',
            'distance',
        )
