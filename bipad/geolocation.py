import os
import geocoder
from federal.models import District

GOOGLE_MAP_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')


def get_city(point):
    return geocoder.google(
        [point.y, point.x],
        components="country:NP",
        method='reverse',
        key=GOOGLE_MAP_API_KEY
    ).city


def get_district(point):
    if point:
        return District.objects.filter(boundary__contains=point).first().title


def get_local_address(point):
    address = get_city(point)
    if not address:
        address = get_district(point)
    return address
