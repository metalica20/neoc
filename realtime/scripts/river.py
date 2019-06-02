import requests
from django.utils import timezone
from realtime.models import River
from django.contrib.gis.geos import Point
from bipad.geolocation import get_local_address
from federal.models import Ward
from alert.models import Alert
from hazard.models import Hazard


current_date = timezone.localtime(timezone.now())


def fetch_river():
    response = requests.get('http://hydrology.gov.np/gss/api/socket/river_watch/response')
    river_data = response.json()
    rivers = []
    for data in river_data:
        water_level_on = None
        water_level_value = None
        point = None

        if data['waterLevel']:
            water_level_value = data['waterLevel']['value']
            water_level_on = data['waterLevel']['datetime']

        if data['longitude']:
            point = Point(float(data['longitude']), float(data['latitude']))

        try:
            warning_level_value = float(data['warning_level'])
        except ValueError:
            warning_level_value = None
        except TypeError:
            warning_level_value = None

        try:
            danger_level_value = float(data['danger_level'])
        except TypeError:
            danger_level_value = None
        except ValueError:
            danger_level_value = None
        if point:
            river = River(
                id=data['id'],
                title=data['name'],
                basin=data['basin'],
                point=point,
                water_level=water_level_value,
                water_level_on=water_level_on,
                danger_level=danger_level_value,
                warning_level=warning_level_value,
                status=data['status'],
                elevation=data['elevation'],
                steady=data['steady'],
                description=data['description'],
                station_series_id=data['series_id'],
            )
            rivers.append(river)
            alert = Alert.objects.filter(reference_type="river", reference_id=data['id']).order_by('-id').first()
            if alert and not alert.expire_on:
                if data['status'] == "BELOW WARNING LEVEL":
                    alert.expire_on = current_date
                    alert.save()
                elif data['status'] == "ABOVE WARNING LEVEL":
                    continue
            if data['status'] == "ABOVE WARNING LEVEL":
                if water_level_on:
                    location = get_local_address(point)
                    wards = Ward.objects.filter(boundary__intersects=point)
                    hazard = Hazard.objects.filter(title_en="Flood").first()
                    alert = Alert(
                        title="Flood warning at %s" % location,
                        source="other",
                        description="Basin: %s \n Elevation: %s \n Warning level: %s \n Water level: %s "
                                    % (
                                        data['basin'],
                                        data['elevation'],
                                        warning_level_value,
                                        water_level_value
                                    ),
                        hazard=hazard,
                        public=True,
                        verified=True,
                        started_on=water_level_on,
                        point=point,
                        reference_type="river",
                        reference_id=data['id']
                    )
                    alert.save()
                    alert.wards.set(wards)

    River.objects.all().delete()
    River.objects.bulk_create(rivers)
