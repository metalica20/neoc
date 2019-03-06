from rest_framework import serializers
from risk_profile.models import Hospital

class HospitalSerializer(serializers.Serializer):

    distance =serializers.SerializerMethodField()
    name= serializers.CharField(max_length=200)
    def get_distance(self,obj):
        return float(''.join([x for x in str(obj.distance) if x!='m']).strip())