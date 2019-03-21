from rest_framework import serializers
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    GeometryField,
)
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from .models import Province, District, Municipality, Ward


class ProvinceGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'boundary'
        model = Province
        fields = '__all__'


class ProvinceSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    bbox = serializers.ListField(read_only=True)
    centroid = GeometryField(read_only=True)

    class Meta:
        model = Province
        exclude = ('boundary',)


class DistrictGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'boundary'
        model = District
        fields = '__all__'


class DistrictSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    bbox = serializers.ListField(read_only=True)
    centroid = GeometryField(read_only=True)

    class Meta:
        model = District
        exclude = ('boundary',)

    expandable_fields = {
        'province': (ProvinceSerializer, {'source': 'province'})
    }


class MunicipalityGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'boundary'
        model = Municipality
        fields = '__all__'


class MunicipalitySerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    bbox = serializers.ListField(read_only=True)
    centroid = GeometryField(read_only=True)

    class Meta:
        model = Municipality
        exclude = ('boundary',)

    expandable_fields = {
        'district': (DistrictSerializer, {'source': 'district'}),
        'province': (ProvinceSerializer, {'source': 'district.province'}),
    }


class WardSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    bbox = serializers.ListField(read_only=True)
    centroid = GeometryField(read_only=True)

    class Meta:
        model = Ward
        exclude = ('boundary',)

    expandable_fields = {
        'municipality': (MunicipalitySerializer, {'source': 'municipality'}),
        'district': (DistrictSerializer, {'source': 'municipality.district'}),
        'province': (ProvinceSerializer, {'source': 'municipality.district.province'}),
    }


class WardGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'boundary'
        model = Ward
        fields = '__all__'

    expandable_fields = {
        'municipality': (MunicipalitySerializer, {'source': 'municipality'}),
        'district': (DistrictSerializer, {'source': 'municipality.district'}),
        'province': (ProvinceSerializer, {'source': 'municipality.district.province'}),
    }
