from rest_framework import viewsets,views
from .models import Hospital,School,LayerTable,SocioEconomicGapanapa,Risk
from incident.models import Incident
from resources.models import Resource,Education,Health
from .serializers import HospitalSerializer,SchoolSerializer,LayerTableSerializer,IncidentSerializer,SociocookSerializer,RiskSerializer
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
import json
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.gis.geos import Point
from .forms import HospitalForm
from hazard.models import Hazard, HazardResources
from django.db.models import Avg, Max, Min, Sum
from django.http import HttpResponse
from django.apps import apps
# import pandas as pd
# Create your views here.
from .geojson_serializer import Serializer


# socio-economic category api

class SociocookViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        a=self.kwargs['field']
        queryset=SocioEconomicGapanapa.objects.filter(name=a)
        serializer=SociocookSerializer(queryset,many=True)
        return Response(serializer.data)


# socio-economic category api

# class SociocookViewSet(viewsets.ModelViewSet):
#     permission_classes=[]
#     serializer_class=SociocookSerializer
#     queryset=SocioEconomicGapanapa.objects.all()

# end

class HospitalViewSet(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=HospitalSerializer
    queryset=Hospital.objects.all()


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=IncidentSerializer
    queryset=Resource.objects.select_related().all()


class ResourceGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        model_name=self.kwargs['m_name']
        object_model=apps.get_model('resources',model_name)
        geojson_serializer = Serializer()
        geojson_serializer.serialize(object_model.objects.all())
        data = geojson_serializer.getvalue()
        resourcegeojson=json.loads(data)
        return Response(resourcegeojson)

# class MarketCenterGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         json_d={}
#         serializers=serialize('geojson',MarketCenter.objects.all(),geometry_field='location',fields=('pk','fid','name','district'))
#         # print(serializers)
#         MarketCentergeojson=json.loads(serializers)
#         json_d['data']=MarketCentergeojson
#         json_d['is_goeserver']=False
#         return Response(MarketCentergeojson)
#
#
# class AirportGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Airport.objects.all(),geometry_field='location',fields=('pk','name'))
#         # print(serializers)
#         Airportgeojson=json.loads(serializers)
#         return Response(Airportgeojson)
#
# class BridgeGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Bridge.objects.all(),geometry_field='location',fields=('pk','name'))
#         # print(serializers)
#         Bridgegeojson=json.loads(serializers)
#         return Response(Bridgegeojson)
#
# class PoliceGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Policestation.objects.all(),geometry_field='location',fields=('pk','name'))
#         # print(serializers)
#         Policestationgeojson=json.loads(serializers)
#         return Response(Policestationgeojson)
#
# class EducationGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Education.objects.all(),geometry_field='location',fields=('pk','name','operator_type','opening_hours','phone_number','email_address','number_of_employees','number_of_students','comments','type'))
#         # print(serializers)
#         Educationgeojson=json.loads(serializers)
#         return Response(Educationgeojson)

class LayerViewset(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=LayerTableSerializer
    queryset=LayerTable.objects.all()


# class BankGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Bank.objects.all(),geometry_field='location',fields=('pk','name','phone_number','email_address','website','opening_hours','operator_type','bank_type','atm_available','Comments'))
#         # print(serializers)
#         Bankgeojson=json.loads(serializers)
#         return Response(Bankgeojson)
#
# class SettlementsGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Settlements.objects.all(),geometry_field='location',fields=('pk','name'))
#         # print(serializers)
#         Settlementsgeojson=json.loads(serializers)
#         return Response(Settlementsgeojson)
#
#
# class HealthGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Health.objects.all(),geometry_field='location',fields=('name','operator_type','opening_hours','phone_number','email_address','emergency_service','icu','nicu','operating_theatre','x_ray','ambulance_service','number_of_staff','number_of_Beds','Comments','type'))
#         # print(serializers)
#         Healthgeojson=json.loads(serializers)
        # return Response(Healthgeojson)

def Dashboard(request):
    if "GET" == request.method:
        return render(request, "dashboard.html")
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return render(request, "dashboard.html")

        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return render(request, "dashboard.html")

        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        fields=Hospital._meta.get_fields()
        print(lines[0])
        # for field in fields:
            # print(field.name)
        for line in lines[1:]:
            csv_colum = line.split(",")
            # print(csv_colum)
            data_dict = {}
            i=0

            for field in fields:

                if(field.name!='id' and field.name!='location'):
                    data_dict[field.name]=csv_colum[i]
                    i=i+1
            data_dict['location']=Point(float(csv_colum[1]),float(csv_colum[0]))
            print('CSV colm', csv_colum[1])
            print('locationnn', data_dict['location'])
            form = HospitalForm(data_dict)
            form.save()

    except Exception as e:
        pass

def count_update(modelname):

    hospital_count = Hospital.objects.all().count()
    LayerTable.objects.get(layer_tbl='Hospital').update(tbl_layer_count=hospital_count)



class IncidentApiView(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=IncidentSerializer
    queryset = HazardResources.objects.all()


class RiskApiView(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        a=self.kwargs['field']
        print(a);
        risk = Risk.objects.all().order_by('-'+a)
        serializer = RiskSerializer(risk ,many=True)
        sum = risk.aggregate(Sum(a))[a+'__sum']
        max = risk.aggregate(Max(a))[a+'__max']
        min = risk.aggregate(Min(a))[a+'__min']
        avg = risk.aggregate(Avg(a))[a+'__avg']
        return Response({'sum':sum if sum else 0 ,'max':max if max else 0 ,'min':min if min else 0 ,'avg':avg if avg else 0,'results':serializer.data})



class NewtestfileViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        a=self.kwargs['field']

        # print(type(obj.a))
        jsonc=SocioEconomicGapanapa.objects.values(a,'name','municipality_id').order_by('-'+a)
        avg=SocioEconomicGapanapa.objects.aggregate(Avg(a))
        summ=SocioEconomicGapanapa.objects.aggregate(Max(a))
        field_avg=a+"__avg"
        field_sum=a+"__max"
        listj={}
        listj['title']="Vulnerability"
        listj['subtitle']="Access"
        listj['sum']=summ[field_sum]
        listj['avg']=avg[field_avg]
        listj['data']=jsonc
        return Response(listj)


class HazardfloodViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        # flood={}
        # basins={}
        # basins['']
        # flood['title']="Flood"
        jsonc={"title":"Flood","about":"For example, the return period of a flood might be 100 years; ( alternatively expressed as its probability of ocurring being 1/100, or 1% in any one year). This does not mean that if a flood with such a return period occurs, then the next will occur in about one hundred years' time - instead, it means that, in any given year, there is a 1% chance that it will happen, regardless of when the last similar event was. Or, put differently, it is 10 times less likely to occur than a flood with a return period of 10 years (or a probability of 10%)",
        "data":{
        "karnali":{
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Karnali_Flood_Depth_5", "center":"[28.491324426181734,81.24904632568361]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Karnali_Flood_Depth_10","center":"[28.491324426181734,81.24904632568361]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Karnali_Flood_Depth_25","center":"[28.491324426181734,81.24904632568361]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Karnali_Flood_Depth_50","center":"[28.491324426181734,81.24904632568361]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Karnali_Flood_Depth_100","center":"[28.491324426181734,81.24904632568361]"},
        },
        "Aurahi":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layername":"Aurahi_Flood_Depth_2","center":"[26.77258726109544,86.00372314453126]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Aurahi_Flood_Depth_5","center":"[26.77258726109544,86.00372314453126]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Aurahi_Flood_Depth_10","center":"[26.77258726109544,86.00372314453126]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Aurahi_Flood_Depth_25","center":"[26.77258726109544,86.00372314453126]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Aurahi_Flood_Depth_50","center":"[26.77258726109544,86.00372314453126]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Aurahi_Flood_Depth_100","center":"[26.77258726109544,86.00372314453126]"},
        },
        "Banganga":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"Banganga_Flood_Depth_2","center":"[27.585361051057333,86.04191780090332]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Banganga_Flood_Depth_5","center":"[27.585361051057333,86.04191780090332]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Banganga_Flood_Depth_10","center":"[27.585361051057333,86.04191780090332]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Banganga_Flood_Depth_25","center":"[27.585361051057333,86.04191780090332]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Banganga_Flood_Depth_50","center":"[27.585361051057333,86.04191780090332]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Banganga_Flood_Depth_100","center":"[27.585361051057333,86.04191780090332]"},
        },
        "Bakraha":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"Bakraha_Flood_Depth_2","center":"[27.585361051057333,86.04191780090332]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Bakraha_Flood_Depth_5","center":"[27.585361051057333,86.04191780090332]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Bakraha_Flood_Depth_10","center":"[27.585361051057333,86.04191780090332]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Bakraha_Flood_Depth_25","center":"[27.585361051057333,86.04191780090332]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Bakraha_Flood_Depth_50","center":"[27.585361051057333,86.04191780090332]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Bakraha_Flood_Depth_100","center":"[27.585361051057333,86.04191780090332]"},
        },
        "Biring":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"Biring_Flood_Depth_2","center":"[26.556593211456345,87.97353744506836]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Biring_Flood_Depth_5","center":"[26.556593211456345,87.97353744506836]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Biring_Flood_Depth_10","center":"[26.556593211456345,87.97353744506836]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Biring_Flood_Depth_25","center":"[26.556593211456345,87.97353744506836]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Biring_Flood_Depth_50","center":"[26.556593211456345,87.97353744506836]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Biring_Flood_Depth_100","center":"[26.556593211456345,87.97353744506836]"},
        },
        "EastRapti":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"EastRapti_Flood_Depth_2","center":"[27.55272061297821,84.70218658447267]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"EastRapti_Flood_Depth_5","center":"[27.55272061297821,84.70218658447267]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"EastRapti_Flood_Depth_10","center":"[27.55272061297821,84.70218658447267]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"EastRapti_Flood_Depth_25","center":"[27.55272061297821,84.70218658447267]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"EastRapti_Flood_Depth_50","center":"[27.55272061297821,84.70218658447267]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"EastRapti_Flood_Depth_100","center":"[27.55272061297821,84.70218658447267]"},
        },
        "Gagan":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"Gagan_Flood_Depth_2","center":"[26.737638715240838,86.38978958129884]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Gagan_Flood_Depth_5","center":"[26.737638715240838,86.38978958129884]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Gagan_Flood_Depth_10","center":"[26.737638715240838,86.38978958129884]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Gagan_Flood_Depth_25","center":"[26.737638715240838,86.38978958129884]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Gagan_Flood_Depth_50","center":"[26.737638715240838,86.38978958129884]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Gagan_Flood_Depth_100","center":"[26.737638715240838,86.38978958129884]"},
        },
        "Jalad":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"Jalad_Flood_Depth_2","center":"[26.811202091464338,86.01024627685547]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Jalad_Flood_Depth_5","center":"[26.811202091464338,86.01024627685547]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Jalad_Flood_Depth_10","center":"[26.811202091464338,86.01024627685547]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Jalad_Flood_Depth_25","center":"[26.811202091464338,86.01024627685547]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Jalad_Flood_Depth_50","center":"[26.811202091464338,86.01024627685547]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Jalad_Flood_Depth_100","center":"[26.811202091464338,86.01024627685547]"},
        },
        "Kankai":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"Kankai_Flood_Depth_2","center":"[26.565498761661104,87.84616470336914]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Kankai_Flood_Depth_5","center":"[26.565498761661104,87.84616470336914]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Kankai_Flood_Depth_10","center":"[26.565498761661104,87.84616470336914]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Kankai_Flood_Depth_25","center":"[26.565498761661104,87.84616470336914]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Kankai_Flood_Depth_50","center":"[26.565498761661104,87.84616470336914]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Kankai_Flood_Depth_100","center":"[26.565498761661104,87.84616470336914]"},
        },
        "Narayani":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"Narayani_Flood_Depth_2","center":"[27.603845382606277,84.22496795654298]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"Narayani_Flood_Depth_5","center":"[27.603845382606277,84.22496795654298]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"Narayani_Flood_Depth_10","center":"[27.603845382606277,84.22496795654298]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"Narayani_Flood_Depth_25","center":"[27.603845382606277,84.22496795654298]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"Narayani_Flood_Depth_50","center":"[27.603845382606277,84.22496795654298]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"Narayani_Flood_Depth_100","center":"[27.603845382606277,84.22496795654298]"},
        },
        "WestRapti":{
        "2":{"returnperiod":"2 year","workspace":"Bipad","layernam":"WestRapti_Flood_Depth_2","center":"[27.95013217159467,82.28313446044922]"},
        "5":{"returnperiod":"5 year","workspace":"Bipad","layername":"WestRapti_Flood_Depth_5","center":"[27.95013217159467,82.28313446044922]"},
        "10":{"returnperiod":"10 year","workspace":"Bipad","layername":"WestRapti_Flood_Depth_10","center":"[27.95013217159467,82.28313446044922]"},
        "25":{"returnperiod":"25 year","workspace":"Bipad","layername":"WestRapti_Flood_Depth_25","center":"[27.95013217159467,82.28313446044922]"},
        "50":{"returnperiod":"50 year","workspace":"Bipad","layername":"WestRapti_Flood_Depth_50","center":"[27.95013217159467,82.28313446044922]"},
        "100":{"returnperiod":"100 year","workspace":"Bipad","layername":"WestRapti_Flood_Depth_100","center":"[27.95013217159467,82.28313446044922]"},
        },
        }}

        return Response(jsonc)


class EarthquakefloodViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        jsonc={"title":"Earthquake","about":"M. Pagani, J. Garcia-Pelaez, R. Gee, K. Johnson, V. Poggi, R. Styron, G. Weatherill, M. Simionato, D. Viganò, L. Danciu, D. Monelli (2018). Global Earthquake Model (GEM) Seismic Hazard Map (version 2018.1 - December 2018), DOI: 10.13117/GEM-GLOBAL-SEISMIC-HAZARD-MAP-2018.1. The Global Earthquake Model (GEM)  depicts the geographic distribution of the Peak Ground Acceleration (PGA) with a 10% probability of being exceeded in 50 years, computed for reference rock conditions (shear wave velocity, VS30, of 760-800 m/s). The map was created by collating maps computed using national and regional probabilistic seismic hazard models developed . Link to the website : https://maps.openquake.org/map/global-seismic-hazard-map/#7/29.299/81.635",
        "data":{
        "GSHM_Earthquake_Map":{
        "Map":{"returnperiod":"Map","workspace":"earthquake", "layername":"earthquake","center":"[28.410728397237914,84.4024658203125]"},

        },
        # "Adrc":{
        #
        # },
        }}

        return Response(jsonc)
