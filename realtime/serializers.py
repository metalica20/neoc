from rest_framework import serializers
from .models import (
    Earthquake,
    River,
    Rain,
    Pollution,
    Fire,
    Weather,
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


class PollutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pollution
        fields = '__all__'


class FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fire
        fields = '__all__'


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
