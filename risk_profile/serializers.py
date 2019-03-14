from rest_framework import serializers
from .models import Hospital,School,LayerTable
from django.shortcuts import get_object_or_404
#from django.contrib.gis.db import models
from risk_profile import models

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields = '__all__'

class LayerTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=LayerTable
        fields = ('layer_name', 'layer_tbl', 'layer_tbl_count','layer_icon','layer_cat','isGeoserver','geoserver_url','geoserver_workspace','public','visibility_level','layer_type','sub_category','upload_type')

    layer_tbl_count = serializers.SerializerMethodField('get_layer_table_count')

    def get_layer_table_count(self, obj):
        # layer_tbl = get_object_or_404(obj.layer_tbl)
        try:
            # print('hello')
            return getattr(models, obj.layer_tbl).objects.all().count()
            # return  model_name.objects.all().count()
            # return getattr(models, obj.layer_tbl).objects.all()
        except Exception as e:
            print('error',e)
            return 0
        # return layer_tbl.count()
