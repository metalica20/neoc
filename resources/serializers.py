from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_polymorphic.serializers import PolymorphicSerializer
from rest_framework import serializers
from .models import (
    Resource,
    Education,
    Health,
    Finance,
    Communication,
    Governance,
    Tourism,
    Industry,
)


class EducationSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('detail', 'polymorphic_ctype')


class HealthSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Health
        exclude = ('detail', 'polymorphic_ctype')


class FinanceSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Finance
        exclude = ('detail', 'polymorphic_ctype')


class CommunicationSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Communication
        exclude = ('detail', 'polymorphic_ctype')


class GovernanceSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Governance
        exclude = ('detail', 'polymorphic_ctype')


class TourismSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Tourism
        exclude = ('detail', 'polymorphic_ctype')


class IndustrySerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Industry
        exclude = ('detail', 'polymorphic_ctype')


class ResourceSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    resource_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='model',
        source='polymorphic_ctype',
    )

    class Meta:
        model = Resource
        exclude = ('detail', 'polymorphic_ctype')


MODEL_SERIALIZER_MAPPING = {
    Education: EducationSerializer,
    Health: HealthSerializer,
    Finance: FinanceSerializer,
    Communication: CommunicationSerializer,
    Governance: GovernanceSerializer,
    Tourism: TourismSerializer,
    Industry: IndustrySerializer,
}


class DetailResourceSerializer(PolymorphicSerializer):
    model_serializer_mapping = MODEL_SERIALIZER_MAPPING

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class ResponseSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
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
        exclude = ('detail', 'polymorphic_ctype')


class DetailResponseSerializer(PolymorphicSerializer):
    model_serializer_mapping = MODEL_SERIALIZER_MAPPING

    def get_distance(self, obj):
        if obj.distance:
            return int(obj.distance.m) or 0
        return None

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['distance'] = self.get_distance(instance)
        return ret
