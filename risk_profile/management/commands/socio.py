import csv
from django.core.management import BaseCommand
from risk_profile.models import SocioEconomicGapanapa
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
                # if(row[10]!='long'):


                # print(row[2])
                    try:
                        education = SocioEconomicGapanapa.objects.create(
                        name=row[0],
                        gn_type=row[1],
                        district=row[2],
                        province=row[3],
                        no_facility_com=row[4],
                        one_atleast_com=row[5],
                        radio_com=row[6],
                        television_com=row[7],
                        cablet_com=row[8],
                        computer_com=row[9],
                        internet_com=row[10],
                        telegraph_com=row[11],
                        mobile_com=row[12],
                        wood_cook=row[13],
                        kerosene_cook=row[14],
                        lpgas_cook=row[15],
                        biogas_cook=row[17],
                        sa_cook=row[16],
                        electricity_cook=row[18],
                        other_cook=row[19],
                        nosta_cook=row[20],
                        electricity_light=row[21],
                        kerosene_light=row[22],
                        biogas_light=row[23],
                        solar_light=row[24],
                        other_light=row[25],
                        nons_light=row[26],
                        tap_water=row[27],
                        tube_water=row[28],
                        cok_water=row[29],
                        unco_water=row[30],
                        spou_water=row[31],
                        river_water=row[32],
                        other_water=row[33],
                        nots_water=row[34],
                        wit_toilet=row[35],
                        flush_toilet=row[36],
                        ordinary_toilet=row[37],
                        not_toilet=row[38]
                        )
                    except:
                        print('error')
