import requests
import datetime
from realtime.models import Fire
from django.contrib.gis.geos import Point
from dateutil import tz
from django.utils import timezone
from django.utils.timezone import localtime
from bipad.settings import TIME_ZONE
from bipad.geolocation import get_local_address
from federal.models import Ward
from alert.models import Alert
from hazard.models import Hazard


ICIMOD_FIRE_QUERY_URL = "http://geoapps.icimod.org/arcgis/rest/services/Nepal/NepalActiveFire/MapServer/0/query"
current_date = timezone.localtime(timezone.now())


def fetch_fire():
    date_to = str(localtime().timestamp()*1000)
    date_from = str((localtime() + datetime.timedelta(-30)).timestamp()*1000)
    params = {
        'time': date_from+','+date_to,
        'outFields': 'OBJECTID,SCAN,ACQ_DATE,ACQ_TIME,CONFIDENCE,LANDCOVER,LATITUDE,LONGITUDE,BRIGHTNESS',
        'f': 'pjson'
    }

    fire_data_url = requests.get(ICIMOD_FIRE_QUERY_URL, params=params)
    fire_data = fire_data_url.json()
    fires = []
    for data in fire_data['features']:
        fire = Fire.objects.all().first()
        if fire.id-data['attributes']['OBJECTID'] > 0:
            point = Point(float(data['attributes']['LONGITUDE']), float(data['attributes']['LATITUDE']))
            event_on = datetime.datetime.fromtimestamp(
                data['attributes']['ACQ_DATE'] / 1000
            ).astimezone(tz.gettz(TIME_ZONE))
            fire = Fire(
                id=data['attributes']['OBJECTID'],
                point=point,
                scan=data['attributes']['SCAN'],
                event_on=event_on,
                brightness=data['attributes']['BRIGHTNESS'],
                confidence=data['attributes']['CONFIDENCE'],
                land_cover=data['attributes']['LANDCOVER'],
            )
            if (current_date-event_on).days < 2:
                Alert.objects.filter(
                    reference_type="fire",
                    reference_id=int(data['attributes']['OBJECTID']),
                ).delete()
                location = get_local_address(point)
                alert_expiry = event_on + datetime.timedelta(1)
                wards = Ward.objects.filter(boundary__intersects=point)
                hazard = Hazard.objects.filter(title_en="Fire").first()
                alert = Alert(
                    title="Fire at %s" % location,
                    source="other",
                    description="Brightness: %s \n Confidence: %s \n Land cover: %s "
                                % (
                                    data['attributes']['BRIGHTNESS'],
                                    data['attributes']['CONFIDENCE'],
                                    data['attributes']['LANDCOVER']
                                ),
                    hazard=hazard,
                    public=True,
                    verified=True,
                    started_on=event_on,
                    expire_on=alert_expiry,
                    point=point,
                    reference_type="fire",
                    reference_id=int(data['attributes']['OBJECTID'])
                )
                alert.save()
                alert.wards.set(wards)
            fires.append(fire)

    Fire.objects.bulk_create(fires)
