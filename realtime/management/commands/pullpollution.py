from django.core.management.base import BaseCommand
from realtime.scripts.pollution import fetch_pollution


class Command(BaseCommand):
    help = 'Import Pollution data from open air quality data API'

    def handle(self, **options):
        fetch_pollution()
