import os
import re
import requests
from bs4 import BeautifulSoup
from realtime.models import Weather
from django.contrib.gis.geos import Point
import geocoder


GOOGLE_MAP_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
WEATHER_URL = "http://mfd.gov.np/weather/"
table_selector = "table", {"class": "table"}


def fetch_weather():
    r = requests.get(WEATHER_URL)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    table_data = soup.find(table_selector).findAll('td')
    map_data = soup.findAll("div", {"class": "weather-icon"})

    map_rows = []
    weathers = []
    table_rows = []
    locations = []

    for weather in map_data:
        temperature_data = re.sub(re.compile('<.*?>'), '', weather['data-pop']).split(" ")
        if weather['title'] not in locations:
            locations.append(weather['title'])
            for data in temperature_data:
                if re.search(r'\d', data):
                    formatted_data = re.sub(re.compile('[a-zA-Z]'), '', data)
                    map_rows.append(formatted_data)

    for data in table_data:
        if "-" in data:
            data = None
            table_rows.append(data)
        else:
            try:
                data = float(data.text)
            except ValueError:
                data = data.text
            table_rows.append(data)

    for i in range(0, int((len(table_rows)-1)/4)):
        coordinates = location_to_coordinates(table_rows[0+i*4])
        if coordinates:
            weather = Weather(
                location=table_rows[0+i*4],
                point=Point(coordinates[1], coordinates[0]),
                maximum_temp=table_rows[1 + i * 4],
                minimum_temp=table_rows[2 + i * 4],
                sunrise=map_rows[0+i*4],
                sunset=map_rows[1+i*4],
                current_temp=map_rows[2+i*4],
                humidity=map_rows[3+i*4],
                rainfall=table_rows[3+i*4],
            )
            weathers.append(weather)
    Weather.objects.all().delete()
    Weather.objects.bulk_create(weathers)


def location_to_coordinates(location):
    coordinates = geocoder.google(location, components="country:NP", key=GOOGLE_MAP_API_KEY).latlng
    return coordinates



