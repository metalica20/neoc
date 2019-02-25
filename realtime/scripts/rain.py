import requests
from realtime.models import Rain
from django.contrib.gis.geos import Point


def fetch_rain():
    response = requests.get('http://hydrology.gov.np/gss/api/socket/rainfall_watch/response')
    river_data = response.json()
    rains = []
    for data in river_data:
        point_value = None

        if data['longitude']:
            point_value = Point(float(data['longitude']), float(data['latitude']))

        rain = Rain(
            id=data['id'],
            title=data['name'],
            basin=data['basin'],
            point=point_value,
            averages=data['averages'],
            status=data['status'],
            elevation=data['elevation'],
            district=data['district'],
            description=data['description'],
            station_series_id=data['series_id'],
        )
        rains.append(rain)
    Rain.objects.all().delete()
    Rain.objects.bulk_create(rains)
