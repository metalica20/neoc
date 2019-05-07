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
from django.apps import apps
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
    # print(GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }'))
    # a=GEOSGeometry('0101000020E61000007C639A19D85B554040F64B4FCEB83B40')
    # print(a.geom_type)

# resources from apps
# resources from apps
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
        all_sum = risk.aggregate(Sum('riskScore'))['riskScore__sum']
        earthquake_risk_max = risk.aggregate(Max('riskScore'))['riskScore__max']
        avg = risk.aggregate(Avg('hdi'))['hdi__avg']
        avg_rem = risk.aggregate(Avg('remoteness'))['remoteness__avg']
        avg_earthquake_risk = risk.aggregate(Avg('riskScore'))['riskScore__avg']
        return Response({'maxriskScore': earthquake_risk_max if earthquake_risk_max else 0 ,'avghdi':avg if avg else 0,'avgremoteness':avg_rem if avg_rem else 0,'avgriskScore':avg_earthquake_risk if avg_earthquake_risk else 0, 'results':serializer.data})



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
        jsonc={"title":"Flood","about":"For example, the return period of a flood might be 100 years; ( alternatively expressed as its probability of ocurring being 1/100, or 1% in any one year). This does not mean that if a flood with such a return period occurs, then the next will occur in about one hundred years' time - instead, it means that, in any given year, there is a 1% chance that it will happen, regardless of when the last similar event was. Or, put differently, it is 10 times less likely to occur than a flood with a return period of 10 years (or a probability of 10%)",
        "data":{
        "karnali":{
        "5":{"returnperiod":"5 year","workspace":"Naxa","layername":"flood_karnali_depth_5", "center":"[28.491324426181734,81.24904632568361]"},
        "10":{"returnperiod":"10 year","workspace":"Naxa","layername":"flood_karnali_depth_10","center":"[28.491324426181734,81.24904632568361]"},
        "25":{"returnperiod":"25 year","workspace":"Naxa","layername":"flood_karnali_depth_25","center":"[28.491324426181734,81.24904632568361]"},
        "50":{"returnperiod":"50 year","workspace":"Naxa","layername":"flood_karnali_depth_50","center":"[28.491324426181734,81.24904632568361]"},
        "100":{"returnperiod":"100 year","workspace":"Naxa","layername":"flood_karnali_depth_100","center":"[28.491324426181734,81.24904632568361]"},
        },
        "Aurahi":{
        "2":{"returnperiod":"2 year","workspace":"Naxa","layername":"flood_aurahi_depth_2","center":"[26.77258726109544,86.00372314453126]"},
        "5":{"returnperiod":"5 year","workspace":"Naxa","layername":"flood_aurahi_depth_5","center":"[26.77258726109544,86.00372314453126]"},
        "10":{"returnperiod":"10 year","workspace":"Naxa","layername":"flood_aurahi_depth_10","center":"[26.77258726109544,86.00372314453126]"},
        "25":{"returnperiod":"25 year","workspace":"Naxa","layername":"flood_aurahi_depth_25","center":"[26.77258726109544,86.00372314453126]"},
        "50":{"returnperiod":"50 year","workspace":"Naxa","layername":"flood_aurahi_depth_50","center":"[26.77258726109544,86.00372314453126]"},
        "100":{"returnperiod":"100 year","workspace":"Naxa","layername":"flood_aurahi_depth_100","center":"[26.77258726109544,86.00372314453126]"},
        },
        "Banganga":{
        "2":{"returnperiod":"2 year","workspace":"Naxa","layernam":"flood_banganga_depth_2","center":"[27.585361051057333,86.04191780090332]"},
        "5":{"returnperiod":"5 year","workspace":"Naxa","layername":"flood_banganga_depth_5","center":"[27.585361051057333,86.04191780090332]"},
        "10":{"returnperiod":"10 year","workspace":"Naxa","layername":"flood_banganga_depth_10","center":"[27.585361051057333,86.04191780090332]"},
        "25":{"returnperiod":"25 year","workspace":"Naxa","layername":"flood_banganga_depth_25","center":"[27.585361051057333,86.04191780090332]"},
        "50":{"returnperiod":"50 year","workspace":"Naxa","layername":"flood_banganga_depth_50","center":"[27.585361051057333,86.04191780090332]"},
        "100":{"returnperiod":"100 year","workspace":"Naxa","layername":"flood_banganga_depth_100","center":"[27.585361051057333,86.04191780090332]"},
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
