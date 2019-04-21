from django.core.management.base import BaseCommand
from realtime.scripts.weather import fetch_weather


class Command(BaseCommand):
    help = 'Import Weather data from Meteorological Forecasting Division'

    def handle(self, **options):
        fetch_weather()
