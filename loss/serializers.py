from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from .models import (
    Loss,
    People,
    Family,
    Infrastructure,
    LivestockType,
    Livestock,
    InfrastructureType,
)


class SimpleLossSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    people_death_count = serializers.IntegerField(
        required=False, read_only=True
    )
    livestock_destroyed_count = serializers.IntegerField(
        required=False, read_only=True
    )
    infrastructure_destroyed_count = serializers.IntegerField(
        required=False, read_only=True
    )

    class Meta:
        model = Loss
        exclude = ('detail',)


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        exclude = ('name',)


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        exclude = ('phone_number',)


class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'


class InfrastructureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureType
        fields = '__all__'


class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = '__all__'


class LivestockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockType
        fields = '__all__'
