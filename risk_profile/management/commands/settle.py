import csv
from django.core.management import BaseCommand
from risk_profile.models import Settlements
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
                # try:
                    Bank = Settlements.objects.create(
                    name=row[1],
                    type=row[0],
                    lat=row[3],
                    long=row[2],
                    location=Point(float(row[2]),float(row[3]))
                    )
                # except:
                    # pass
