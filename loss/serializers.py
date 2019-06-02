from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from .models import (
    Loss,
    People,
    Family,
    Infrastructure,
    Agriculture,
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


class AgricultureSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Agriculture
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
    people_death_male_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_death_female_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_death_unknown_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_death_disabled_count = serializers.IntegerField(
        required=False, read_only=True
    )

    people_missing_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_missing_male_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_missing_female_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_missing_unknown_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_missing_disabled_count = serializers.IntegerField(
        required=False, read_only=True
    )

    people_injured_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_injured_male_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_injured_female_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_injured_unknown_count = serializers.IntegerField(
        required=False, read_only=True
    )
    people_injured_disabled_count = serializers.IntegerField(
        required=False, read_only=True
    )

    livestock_destroyed_count = serializers.IntegerField(
        required=False, read_only=True
    )
    infrastructure_destroyed_count = serializers.IntegerField(
        required=False, read_only=True
    )
    infrastructure_destroyed_house_count = serializers.IntegerField(
        required=False, read_only=True
    )
    infrastructure_affected_house_count = serializers.IntegerField(
        required=False, read_only=True
    )

    infrastructure_economic_loss = serializers.IntegerField(
        required=False, read_only=True
    )
    agriculture_economic_loss = serializers.IntegerField(
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
        'agricultures': (AgricultureSerializer, {'source': 'agricultures', 'many': True}),
    }
