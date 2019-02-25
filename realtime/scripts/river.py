from realtime.models import River
from django.contrib.gis.geos import Point
import requests


def fetch_river():
    response = requests.get('http://hydrology.gov.np/gss/api/socket/river_watch/response')
    river_data = response.json()
    rivers = []
    for data in river_data:
        water_level_datetime = None
        water_level_value = None
        point_value = None

        if data['waterLevel']:
            water_level_value=data['waterLevel']['value']
            water_level_datetime=data['waterLevel']['datetime']

        if data['longitude']:
            point_value = Point(float(data['longitude']), float(data['latitude']))

        try:
            warning_level_value = float(data['warning_level'])
        except ValueError:
            warning_level_value = None
        except TypeError:
            warning_level_value = None

        try:
            danger_level_value = float(data['danger_level'])
        except TypeError:
            danger_level_value= None
        except ValueError:
            danger_level_value = None

        river = River(
            id=data['id'],
            title=data['name'],
            basin=data['basin'],
            point=point_value,
            water_level_value=water_level_value,
            water_level_datetime=water_level_datetime,
            danger_level=danger_level_value,
            warning_level=warning_level_value,
            status=data['status'],
            elevation=data['elevation'],
            steady=data['steady'],
            description=data['description'],
            station_series_id=data['series_id'],
        )
        rivers.append(river)
    River.objects.all().delete()
    River.objects.bulk_create(rivers)


