from rest_framework import viewsets,views
from .models import Hospital,School,MarketCenter,LayerTable,Airport,Bridge,Policestation,Education,Bank,Settlements,SocioEconomicGapanapa,Risk,Health
from incident.models import Incident
from resources.models import Resource
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
# import pandas as pd
# Create your views here.
from .geojson_serializer import Serializer


# socio-economic category api

class SociocookViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        a=self.kwargs['field']
        print(a);
        queryset=SocioEconomicGapanapa.objects.filter(name=a)
        serializer=SociocookSerializer(queryset,many=True)
        return Response(serializer.data)
        # queryset=SocioEconomicGapanapa.objects.all()
        # serializers=serialize(queryset)
        # MarketCentergeojson=json.loads(serializers)
        #
        # # serializer_class=SociocookSerializer
        # listt=[]
        #
        # listt['data']=q
    # def get_queryset(self):





# end

class HospitalViewSet(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=HospitalSerializer
    queryset=Hospital.objects.all()


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=IncidentSerializer
    queryset=Resource.objects.select_related().all()
    # print(GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }'))
    # a=GEOSGeometry('0101000020E61000007C639A19D85B554040F64B4FCEB83B40')
    # print(a.geom_type)

class HospitalGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        # json_d={}
        # print(Health.objects.all().values('title','bed_count'))
        # serializers=serialize('custom_geojson',Health.objects.all(),geometry_field='point',fields=('pk','ward','title','description','type','bed_count'))
        # # print(serializers)
        # hospitalgeojson=json.loads(serializers)
        # json_d['data']=hospitalgeojson
        # json_d['is_goeserver']=False
        # return Response(hospitalgeojson)
        geojson_serializer = Serializer()
        geojson_serializer.serialize(Health.objects.all())
        data = geojson_serializer.getvalue()
        hospitalgeojson=json.loads(data)

        return Response(hospitalgeojson)

class MarketCenterGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        json_d={}
        serializers=serialize('geojson',MarketCenter.objects.all(),geometry_field='location',fields=('pk','fid','name','district'))
        # print(serializers)
        MarketCentergeojson=json.loads(serializers)
        json_d['data']=MarketCentergeojson
        json_d['is_goeserver']=False
        return Response(MarketCentergeojson)

# class AirportGeojsonViewSet(views.APIView):
#     permission_classes=[]
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Airport.objects.all(),geometry_field='location',fields=('name'))
#         # print(serializers)
#         Airportgeojson=json.loads(serializers)
#         return Response(Airportgeojson)

class AirportGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Airport.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Airportgeojson=json.loads(serializers)
        return Response(Airportgeojson)

class BridgeGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Bridge.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Bridgegeojson=json.loads(serializers)
        return Response(Bridgegeojson)

class PoliceGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Policestation.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Policestationgeojson=json.loads(serializers)
        return Response(Policestationgeojson)

class EducationGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Education.objects.all(),geometry_field='location',fields=('pk','name','operator_type','opening_hours','phone_number','email_address','number_of_employees','number_of_students','comments','type'))
        # print(serializers)
        Educationgeojson=json.loads(serializers)
        return Response(Educationgeojson)

class LayerViewset(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=LayerTableSerializer
    queryset=LayerTable.objects.all()


class BankGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Bank.objects.all(),geometry_field='location',fields=('pk','name','phone_number','email_address','website','opening_hours','operator_type','bank_type','atm_available','Comments'))
        # print(serializers)
        Bankgeojson=json.loads(serializers)
        return Response(Bankgeojson)

class SettlementsGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Settlements.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Settlementsgeojson=json.loads(serializers)
        return Response(Settlementsgeojson)


class HealthGeojsonViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Health.objects.all(),geometry_field='location',fields=('name','operator_type','opening_hours','phone_number','email_address','emergency_service','icu','nicu','operating_theatre','x_ray','ambulance_service','number_of_staff','number_of_Beds','Comments','type'))
        # print(serializers)
        Healthgeojson=json.loads(serializers)
        return Response(Healthgeojson)

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
                    # print(field.name)
                    # print(csv_colum[i])
                    data_dict[field.name]=csv_colum[i]
                    i=i+1
                    # print(csv_colum[1])

            # print(float(csv_colum[1]))
            # print(csv_colum[0])
            # print(Point(float(csv_colum[1]),float(csv_colum[0])))
            data_dict['location']=Point(float(csv_colum[1]),float(csv_colum[0]))
            # data_dict['location']=GEOSGeometry('POINT('float(csv_colum[1]) float(csv_colum[0])')')
            print('CSV colm', csv_colum[1])
            print('locationnn', data_dict['location'])
            form = HospitalForm(data_dict)
            form.save()


        # count_update('Hospital')
        # return render(request, "dashboard.html")





    except Exception as e:
        pass

def count_update(modelname):

    hospital_count = Hospital.objects.all().count()
    LayerTable.objects.get(layer_tbl='Hospital').update(tbl_layer_count=hospital_count)



class IncidentApiView(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=IncidentSerializer
    queryset = HazardResources.objects.all()
    # permission_classes=(IsAuthenticated,)
    # def get(self,request,*args,**kwargs):
    #     incident = request.GET['incident']
    #
    #     serializer = IncidentSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def get(self, request, *args, **kwargs):
    #     incident = request.GET['incident']
    #     i = Incident.objects.get(pk=incident)
    #     hazard = Hazard.objects.get(id=i.hazard_id)
    #     print(hazard)
    #     # serializers=serialize('json',Incident.objects.get(pk=incident),fields=('pk','title'))
    #     datajson=json.loads(i)
    #
    #     # serializers=serialize('json', HazardResources.objects.filter(hazard=hazard).select_related('resource'), fields=('resource', ))
    #     # print(serializers)
    #     # incidentjson=json.loads(serializers)
    #     return Response(datajson)

# class RiskApiView(viewsets.ModelViewSet):
#     permission_classes=[]
#     serializer_class=RiskSerializer
#     queryset = Risk.objects.all()
class RiskApiView(views.APIView):
    permission_classes=[]
    # serializer_class=RiskSerializer
    # queryset = Risk.objects.all()
    def get(self, request):
        risk = Risk.objects.all().order_by('-hdi')
        serializer = RiskSerializer(risk ,many=True)
        print(serializer.data)
        all_sum = risk.aggregate(Sum('hdi'))['hdi__sum']
        avg = risk.aggregate(Avg('hdi'))['hdi__avg']
        return Response({'sum': all_sum if all_sum else 0 ,'avg':avg if avg else 0, 'results':serializer.data})



class NewtestfileViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        a=self.kwargs['field']

        # print(type(obj.a))

        jsonc=SocioEconomicGapanapa.objects.values(a,'name','municipality_id').order_by('-'+a)
        avg=SocioEconomicGapanapa.objects.aggregate(Avg(a))
        summ=SocioEconomicGapanapa.objects.aggregate(Max(a))

        # jsonc=SocioEconomicGapanapa.objects.all()
        # print('jsoncccc',a)
        # print('jsoncc', jsonc)
        # d='data.a';
        field_avg=a+"__avg"
        field_sum=a+"__max"
        listj={}

        # listk={}

        listj['title']="Vulnerability"
        listj['subtitle']="Access"
        listj['sum']=summ[field_sum]
        listj['avg']=avg[field_avg]
        # for data in jsonc:
        #     listk[data.district]=data.lpgas_cook
        listj['data']=jsonc
        # print(listj)
        return Response(listj)


class HazardfloodViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        # flood={}
        # basins={}
        # basins['']
        # flood['title']="Flood"
        jsonc={"title":"flood","data":{
        "karnali":{
        "5":{"returnperiod":"5 year","workspace":"Naxa:flood_karnali_depth_5","center":"[28.491324426181734,81.24904632568361]"},
        "10":{"returnperiod":"10 year","workspace":"Naxa:flood_karnali_depth_10","center":"[28.491324426181734,81.24904632568361]"},
        "25":{"returnperiod":"25 year","workspace":"Naxa:flood_karnali_depth_25","center":"[28.491324426181734,81.24904632568361]"},
        "50":{"returnperiod":"50 year","workspace":"Naxa:flood_karnali_depth_50","center":"[28.491324426181734,81.24904632568361]"},
        "100":{"returnperiod":"100 year","workspace":"Naxa:flood_karnali_depth_100","center":"[28.491324426181734,81.24904632568361]"},
        },
        "Aurahi":{
        "2":{"returnperiod":"2 year","workspace":"Naxa:flood_aurahi_depth_2","center":"[26.77258726109544,86.00372314453126]"},
        "5":{"returnperiod":"5 year","workspace":"Naxa:flood_aurahi_depth_5","center":"[26.77258726109544,86.00372314453126]"},
        "10":{"returnperiod":"10 year","workspace":"Naxa:flood_aurahi_depth_10","center":"[26.77258726109544,86.00372314453126]"},
        "25":{"returnperiod":"25 year","workspace":"Naxa:flood_aurahi_depth_25","center":"[26.77258726109544,86.00372314453126]"},
        "50":{"returnperiod":"50 year","workspace":"Naxa:flood_aurahi_depth_50","center":"[26.77258726109544,86.00372314453126]"},
        "100":{"returnperiod":"100 year","workspace":"Naxa:flood_aurahi_depth_100","center":"[26.77258726109544,86.00372314453126]"},
        },
        "Banganga":{
        "2":{"returnperiod":"2 year","workspace":"Naxa:flood_banganga_depth_2","center":"[27.585361051057333,86.04191780090332]"},
        "5":{"returnperiod":"5 year","workspace":"Naxa:flood_banganga_depth_5","center":"[27.585361051057333,86.04191780090332]"},
        "10":{"returnperiod":"10 year","workspace":"Naxa:flood_banganga_depth_10","center":"[27.585361051057333,86.04191780090332]"},
        "25":{"returnperiod":"25 year","workspace":"Naxa:flood_banganga_depth_25","center":"[27.585361051057333,86.04191780090332]"},
        "50":{"returnperiod":"50 year","workspace":"Naxa:flood_banganga_depth_50","center":"[27.585361051057333,86.04191780090332]"},
        "100":{"returnperiod":"100 year","workspace":"Naxa:flood_banganga_depth_100","center":"[27.585361051057333,86.04191780090332]"},
        },
        }}

        return Response(jsonc)


class EarthquakefloodViewSet(views.APIView):
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        # flood={}
        # basins={}
        # basins['']
        # flood['title']="Flood"
        jsonc={"title":"Earthquake","data":{
        "Openquake":{
        "Map":{"returnperiod":"Map","workspace":"earthquake","center":"[28.408312587374258,84.40521240234376]"},

        },
        "Adrc":{

        },
        }}

        return Response(jsonc)
