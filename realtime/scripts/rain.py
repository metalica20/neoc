import requests
from realtime.models import Rain
from django.utils import timezone
from django.contrib.gis.geos import Point
from federal.models import Ward
from alert.models import Alert
from hazard.models import Hazard
from bipad.geolocation import get_local_address


current_date = timezone.localtime(timezone.now())


def fetch_rain():
    response = requests.get('http://hydrology.gov.np/gss/api/socket/rainfall_watch/response')
    river_data = response.json()
    rains = []
    for data in river_data:
        point = None

        if data['longitude']:
            point = Point(float(data['longitude']), float(data['latitude']))

        # Clean averages values
        averages = data['averages']
        for average in averages:
            average['interval'] = int(average['interval'])
            if average['value'] == 'N/A':
                average['value'] = None

        rain = Rain(
            id=data['id'],
            title=data['name'],
            basin=data['basin'],
            point=point,
            averages=averages,
            status=data['status'],
            elevation=data['elevation'],
            description=data['description'],
            station_series_id=data['series_id'],
        )
        rains.append(rain)
        alert = Alert.objects.filter(reference_type="rain", reference_id=data['id']).order_by('-id').first()
        if alert and not alert.expire_on:
            if data['status'] == "BELOW WARNING LEVEL":
                alert.expire_on = current_date
                alert.save()
            elif data['status'] == "ABOVE WARNING LEVEL":
                continue
        if data['status'] == "ABOVE WARNING LEVEL":
            location = get_local_address(point)
            wards = Ward.objects.filter(boundary__intersects=point)
            hazard = Hazard.objects.filter(title_en="Heavy Rainfall").first()
            alert = Alert(
                title="Heavy Rainfall at %s" % location,
                source="other",
                description="Basin: %s \n Elevation: %s \n Averages: %s "
                            % (
                                data['basin'],
                                data['elevation'],
                                averages,
                            ),
                hazard=hazard,
                public=True,
                verified=True,
                started_on=current_date,
                point=point,
                reference_type="rain",
                reference_id=data['id']
            )
            alert.save()
            alert.wards.set(wards)
    Rain.objects.all().delete()
    Rain.objects.bulk_create(rains)
