from django.core.management.base import BaseCommand
from resources.scripts.hospital import import_hospital


class Command(BaseCommand):
    help = 'Import Hospital data from shape files'

    def handle(self, **options):
        import_hospital()
