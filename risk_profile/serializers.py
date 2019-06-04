from rest_framework import serializers
<<<<<<< HEAD
from .models import Hospital,School,LayerTable,SocioEconomicGapanapa,Risk,HazardType,HazardLayer,HazardSubLayer,ExposureLayer,ExposureType
=======
from .models import Hospital,School,LayerTable,SocioEconomicGapanapa,Risk,HazardType,HazardLayer,HazardSubLayer,HazardSubLayerDetail
>>>>>>> 2c974129632fef35a8bc5ee562383817077e9b6b
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

<<<<<<< HEAD
# class HazardSubLayerDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=HazardSubLayerDetail
#         fields = ('returnperiod','workspace')

class HazardSubLayerSerializer(serializers.ModelSerializer):
    # HazardSubLayerDetail= HazardSubLayerDetailSerializer(many=True, read_only=True)
    class Meta:
        model=HazardSubLayer
        fields = ('__all__')
=======
class HazardSubLayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=HazardSubLayerDetail
        fields = ('returnperiod','workspace')

class HazardSubLayerSerializer(serializers.ModelSerializer):
    HazardSubLayerDetail= HazardSubLayerDetailSerializer(many=True, read_only=True)
    class Meta:
        model=HazardSubLayer
        fields = ('hazard_subLayer','HazardSubLayerDetail')
>>>>>>> 2c974129632fef35a8bc5ee562383817077e9b6b

class HazardlayerSerializer(serializers.ModelSerializer):
    HazardSubLayer= HazardSubLayerSerializer(many=True, read_only=True)
    class Meta:
        model=HazardLayer
<<<<<<< HEAD
        fields = ('title','about','HazardSubLayer')
=======
        fields = ('title','HazardSubLayer')
>>>>>>> 2c974129632fef35a8bc5ee562383817077e9b6b

class HazardtypeSerializer(serializers.ModelSerializer):
    HazardLayer= HazardlayerSerializer(many=True, read_only=True)
    class Meta:
        model=HazardType
        fields = ('id', 'title', 'about', 'HazardLayer')
<<<<<<< HEAD


class ExposurelayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExposureLayer  
        fields = ('__all__')

class ExposuretypeSerializer(serializers.ModelSerializer):
    ExposureLayer= ExposurelayerSerializer(many=True, read_only=True)
    class Meta:
        model=ExposureType  
        fields = ('id', 'title', 'about', 'ExposureLayer')
=======
>>>>>>> 2c974129632fef35a8bc5ee562383817077e9b6b


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields= '__all__'


class SociocookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocioEconomicGapanapa
        fields= '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model= HazardResources
        fields = '__all__'


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Risk
        fields = ('__all__')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields = '__all__'

class LayerTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=LayerTable
        fields = ('layer_name', 'layer_tbl', 'layer_tbl_count','type','layer_icon','layer_cat','isGeoserver','geoserver_url','geoserver_workspace','public','visibility_level','layer_type','sub_category','upload_type')

    layer_tbl_count = serializers.SerializerMethodField('get_layer_table_count')
    type = serializers.SerializerMethodField()

    def get_layer_table_count(self, obj):
        try:
            # print('hello')
            return getattr(resources.models, obj.layer_tbl).objects.all().count()
        except Exception as e:
            print('error',e)
            return 0
    def get_type(self,obj):
        try:
            return getattr(resources.models, obj.layer_tbl).objects.values('type').distinct()
        except Exception as e:
            print('error',e)
            return 0
