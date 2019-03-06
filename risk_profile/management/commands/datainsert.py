import csv
from django.core.management import BaseCommand
from risk_profile.models import Hospital,School
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
                if(row[8]!='LONGITUDE'):
                    hospital = Hospital.objects.create(
                        fid=row[0],
                        name=row[3],
                        district=row[4],
                        vdc=row[5],
                        ward=row[6],
                        type=row[10],
                        lat=row[7],
                        long=row[8],
                        location=Point(float(row[8]),float(row[7]))



                )
