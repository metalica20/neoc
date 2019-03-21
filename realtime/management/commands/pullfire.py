from django.core.management.base import BaseCommand
from realtime.scripts.fire import fetch_fire


class Command(BaseCommand):
    help = 'Import fire data from ICIMOD rest API'

    def handle(self, **options):
        fetch_fire()
