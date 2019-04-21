from django.core.management.base import BaseCommand
from federal.scripts.generate_boundary import generate_boundary


class Command(BaseCommand):
    help = 'Generate municipality, district and province boundary from wards boundary'

    def handle(self, **options):
        generate_boundary()
