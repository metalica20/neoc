from rest_framework import serializers
from risk_profile.models import Hospital

class HospitalSerializer(serializers.Serializer):

    distance =serializers.SerializerMethodField()
    name= serializers.CharField(max_length=200)
    lat= serializers.CharField(max_length=200)
    long= serializers.CharField(max_length=200)
    def get_distance(self,obj):
        a=float(''.join([x for x in str(obj.distance) if x != 'm']).strip())/1000

        return str("{0:.3f}".format(a)) +'km'