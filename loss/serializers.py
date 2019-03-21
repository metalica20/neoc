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


class LivestockTypeSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = LivestockType
        fields = '__all__'


class InfrastructureTypeSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = InfrastructureType
        fields = '__all__'


class PeopleSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = People
        exclude = ('name', 'created_on', 'modified_on')  # TODO: discuss confidentiality


class FamilySerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Family
        exclude = ('phone_number', 'created_on', 'modified_on')  # TODO: discuss confidentiality


class InfrastructureSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = Infrastructure
        exclude = ('created_on', 'modified_on')


class LivestockSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    type = serializers.StringRelatedField()

    class Meta:
        model = Livestock
        fields = '__all__'


class LossSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
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

    expandable_fields = {
        'peoples': (PeopleSerializer, {'source': 'peoples', 'many': True}),
        'families': (FamilySerializer, {'source': 'families', 'many': True}),
        'livestocks': (LivestockSerializer, {'source': 'livestocks', 'many': True}),
        'infrastructures': (InfrastructureSerializer, {'source': 'infrastructures', 'many': True}),
    }
