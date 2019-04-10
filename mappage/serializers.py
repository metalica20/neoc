import io
from rest_framework.parsers import JSONParser

from rest_framework import serializers
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from rest_framework.renderers import JSONRenderer

from risk_profile.models import Hospital

from hazard.models import HazardResources


class ModelSerializer(serializers.Serializer):

    distance = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    geometry = serializers.SerializerMethodField()

    def get_distance(self, obj):
        dist = float(''.join([x for x in str(obj.distance) if x != 'm']).strip())/1000

        return str("{0:.3f}".format(dist)) +'km'

    def get_geometry(self, obj):
        return {"type": "Point", "coordinates": [float(obj.point.y), float(obj.point.x)]}

    def get_name(self, obj):
        return obj.title


class HospitalSerializer(serializers.Serializer):

    distance =serializers.SerializerMethodField()
    name= serializers.CharField(max_length=200)
    lat= serializers.CharField(max_length=200)
    long= serializers.CharField(max_length=200)
    def get_distance(self,obj):
        a=float(''.join([x for x in str(obj.distance) if x != 'm']).strip())/1000

        return str("{0:.3f}".format(a)) +'km'


class HazardResourceSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    resources = serializers.SerializerMethodField()

    class Meta:
        model = HazardResources
        fields = ('id', 'name', 'resources')

    def get_name(self, obj):
        return obj.resource.model.title()

    def get_resources(self, obj):
        user_location = self.context['user_location']
        count = self.context['count']
        max_distance = self.context['max_distance']
        model_x = obj.resource.model_class()

        resource_queryset = model_x.objects.filter(point__distance_lte=(user_location, D(km=max_distance))).\
            annotate(distance=Distance('point', user_location)).order_by('distance')[0:int(count)]
        resource_json = ModelSerializer(resource_queryset, many=True)
        json = JSONRenderer().render(resource_json.data)
        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)

        return data

