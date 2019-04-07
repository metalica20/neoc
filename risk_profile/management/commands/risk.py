import csv
from django.core.management import BaseCommand
from risk_profile.models import Risk
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            # print(reader)

            for row in reader:
                # print(row[2])
                try:
                    Bank = Risk.objects.create(
                    district=row[0],
                    remoteness=row[1],
                    hdi=row[2],
                    riskScore=row[3],
                    )
                except:
                    print('error')
