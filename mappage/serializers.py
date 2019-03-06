from rest_framework import serializers
from risk_profile.models import Hospital

class HospitalSerializer(serializers.ModelSerializer):

    distance =serializers.SerializerMethodField()
    class Meta:
        model = Hospital
        fields= '__all__'
    
    def get_distance(self,obj):
        return str(obj.distance)
