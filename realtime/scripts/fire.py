import requests
import datetime
from realtime.models import Fire
from django.contrib.gis.geos import Point
from dateutil import tz
from django.utils.timezone import localtime
from bipad.settings import TIME_ZONE

ICIMOD_FIRE_QUERY_URL = "http://geoapps.icimod.org/arcgis/rest/services/Nepal/NepalActiveFire/MapServer/0/query"


def fetch_fire():
    date_to = str(localtime().timestamp()*1000)
    date_from = str((localtime() + datetime.timedelta(-30)).timestamp()*1000)
    params = {
        'time': date_from+','+date_to,
        'outFields': 'SCAN,ACQ_DATE,ACQ_TIME,CONFIDENCE,LANDCOVER,LATITUDE,LONGITUDE,BRIGHTNESS',
        'f': 'pjson'
    }

    fire_data_url = requests.get(ICIMOD_FIRE_QUERY_URL, params=params)
    fire_data = fire_data_url.json()
    fires = []
    for data in fire_data['features']:

        fire = Fire(
            point=Point(float(data['attributes']['LONGITUDE']), float(data['attributes']['LATITUDE'])),
            scan=data['attributes']['SCAN'],
            event_on=datetime.datetime.fromtimestamp(
                data['attributes']['ACQ_DATE'] / 1000).astimezone(tz.gettz(TIME_ZONE)),
            brightness=data['attributes']['BRIGHTNESS'],
            confidence=data['attributes']['CONFIDENCE'],
            land_cover=data['attributes']['LANDCOVER'],
        )
        fires.append(fire)

    Fire.objects.all().delete()
    Fire.objects.bulk_create(fires)
