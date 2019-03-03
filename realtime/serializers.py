from rest_framework import serializers
from .models import (
    Earthquake,
    River,
    Rain,
)


class EarthquakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earthquake
        fields = '__all__'


class RiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River
        exclude = ('station_series_id',)


class RainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rain
        exclude = ('station_series_id',)
