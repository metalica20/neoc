import csv
from django.core.management import BaseCommand
from risk_profile.models import MarketCenter
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
            # print(type(reader))
            for row in reader:
                if(row[15]!='Y'):

                        market = MarketCenter.objects.create(
                        fid=row[0],
                        name=row[19],
                        district=row[16],
                        vdc=row[17],
                        ward=row[20],
                        wholesale=row[25],
                        commodity=row[29],
                        lat=row[15],
                        long=row[14],
                        location=Point(float(row[14]),float(row[15]))



                )
