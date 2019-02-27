from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()
    resource_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='model',
        source='polymorphic_ctype',
    )

    def get_distance(self, obj):
        return int(obj.distance.m)

    class Meta:
        model = Resource
        fields = ('title', 'description', 'point',
                  'ward', 'resource_type', 'distance')
