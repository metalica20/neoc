from django.core.management.base import BaseCommand
from realtime.scripts.rain import fetch_rain


class Command(BaseCommand):
    help = 'Import rain data from DHM api'

    def handle(self, **options):
        fetch_rain()
