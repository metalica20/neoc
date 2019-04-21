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
                        province_id=row[0],
                        district_id=row[1],
                        municipality_id=row[2],
                        name=row[3],
                        gn_type=row[4],
                        district=row[5],
                        no_facility_com=row[6],
                        one_atleast_com=row[7],
                        radio_com=row[8],
                        television_com=row[9],
                        cablet_com=row[10],
                        computer_com=row[11],
                        internet_com=row[12],
                        telephone_com=row[13],
                        mobile_com=row[14],
                        wood_cook=row[15],
                        kerosene_cook=row[16],
                        lpgas_cook=row[17],
                        sa_cook=row[18],
                        biogas_cook=row[19],
                        electricity_cook=row[20],
                        other_cook=row[21],
                        nosta_cook=row[22],
                        electricity_light=row[23],
                        kerosene_light=row[24],
                        biogas_light=row[25],
                        solar_light=row[26],
                        other_light=row[27],
                        nons_light=row[28],
                        tap_water=row[29],
                        tube_water=row[30],
                        cok_water=row[31],
                        unco_water=row[32],
                        spou_water=row[33],
                        river_water=row[34],
                        other_water=row[35],
                        nots_water=row[36],
                        wit_toilet=row[37],
                        flush_toilet=row[38],
                        ordinary_toilet=row[39],
                        not_toilet=row[40]
                        )
                    except:
                        print('error')
