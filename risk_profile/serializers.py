from rest_framework import serializers
from .models import Hospital,School,CapacityResources,MunicipalityLevelVulnerability,DistrictLevelVulnerability,HazardType,HazardLayer,HazardSubLayer,ExposureLayer,ExposureType
from incident.models import Incident
from resources.models import Resource
from hazard.models import Hazard, HazardResources
from django.shortcuts import get_object_or_404
#from django.contrib.gis.db import models
from risk_profile import models
from django.core.serializers.json import DjangoJSONEncoder
from resources.models import Resource
import resources
import django

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields = ('__all__')

# class HazardSubLayerDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=HazardSubLayerDetail
#         fields = ('returnperiod','workspace')

class HazardSubLayerSerializer(serializers.ModelSerializer):
    # HazardSubLayerDetail= HazardSubLayerDetailSerializer(many=True, read_only=True)
    class Meta:
        model=HazardSubLayer
        fields = ('__all__')

class HazardlayerSerializer(serializers.ModelSerializer):
    HazardSubLayer= HazardSubLayerSerializer(many=True, read_only=True)
    class Meta:
        model=HazardLayer
        fields = ('title','about','HazardSubLayer')

class HazardtypeSerializer(serializers.ModelSerializer):
    HazardLayer= HazardlayerSerializer(many=True, read_only=True)
    class Meta:
        model=HazardType
        fields = ('id', 'title', 'about','hazard_icon','HazardLayer')


class ExposurelayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExposureLayer  
        fields = ('__all__')

class ExposuretypeSerializer(serializers.ModelSerializer):
    ExposureLayer= ExposurelayerSerializer(many=True, read_only=True)
    class Meta:
        model=ExposureType  
        fields = ('id', 'title', 'about', 'ExposureLayer')


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields= '__all__'


class SociocookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalityLevelVulnerability
        fields= '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model= HazardResources
        fields = '__all__'


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model= DistrictLevelVulnerability
        fields = ('__all__')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields = '__all__'

class LayerTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=CapacityResources
        fields = ('title','layername', 'layer_tbl_count','type','layer_icon','isGeoserver','geoserver_url','geoserver_workspace','public','filter_options')

    layer_tbl_count = serializers.SerializerMethodField('get_layer_table_count')
    type = serializers.SerializerMethodField()

    def get_layer_table_count(self, obj):
        try:
            # print('hello')
            return getattr(resources.models, obj.layername).objects.all().count()
        except Exception as e:
            print('error',e)
            return 0
    def get_type(self,obj):
        try:
            return getattr(resources.models, obj.layername).objects.values('type').distinct()
        except Exception as e:
            print('error',e)
            return 0
