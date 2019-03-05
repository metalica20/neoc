from rest_framework import serializers
from .models import Hospital,School

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields = '__all__'
