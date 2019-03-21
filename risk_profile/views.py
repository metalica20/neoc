from rest_framework import viewsets,views
from .models import Hospital,School,MarketCenter,LayerTable,Airport,Bridge,Policestation,Education,Bank,Settlements
from incident.models import Incident
from resources.models import Resource
from .serializers import HospitalSerializer,SchoolSerializer,LayerTableSerializer,IncidentSerializer
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
# import pandas as pd
# Create your views here.

class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class=HospitalSerializer
    queryset=Hospital.objects.all()


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class=IncidentSerializer
    queryset=Resource.objects.select_related().all()
    # print(GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }'))
    # a=GEOSGeometry('0101000020E61000007C639A19D85B554040F64B4FCEB83B40')
    # print(a.geom_type)

class HospitalGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        json_d={}
        serializers=serialize('geojson',Hospital.objects.all(),geometry_field='location',fields=('pk','fid','name','district','type'))
        # print(serializers)
        hospitalgeojson=json.loads(serializers)
        json_d['data']=hospitalgeojson
        json_d['is_goeserver']=False
        return Response(hospitalgeojson)

class MarketCenterGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        json_d={}
        serializers=serialize('geojson',MarketCenter.objects.all(),geometry_field='location',fields=('pk','fid','name','district'))
        # print(serializers)
        MarketCentergeojson=json.loads(serializers)
        json_d['data']=MarketCentergeojson
        json_d['is_goeserver']=False
        return Response(MarketCentergeojson)

# class AirportGeojsonViewSet(views.APIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self,request,*args,**kwargs):
#         serializers=serialize('geojson',Airport.objects.all(),geometry_field='location',fields=('name'))
#         # print(serializers)
#         Airportgeojson=json.loads(serializers)
#         return Response(Airportgeojson)

class AirportGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Airport.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Airportgeojson=json.loads(serializers)
        return Response(Airportgeojson)

class BridgeGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Bridge.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Bridgegeojson=json.loads(serializers)
        return Response(Bridgegeojson)

class PoliceGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Policestation.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Policestationgeojson=json.loads(serializers)
        return Response(Policestationgeojson)

class EducationGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Education.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Educationgeojson=json.loads(serializers)
        return Response(Educationgeojson)

class LayerViewset(viewsets.ModelViewSet):
    serializer_class=LayerTableSerializer
    queryset=LayerTable.objects.all()


class BankGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Bank.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Bankgeojson=json.loads(serializers)
        return Response(Bankgeojson)

class SettlementsGeojsonViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        serializers=serialize('geojson',Settlements.objects.all(),geometry_field='location',fields=('pk','name'))
        # print(serializers)
        Settlementsgeojson=json.loads(serializers)
        return Response(Settlementsgeojson)

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
    serializer_class=IncidentSerializer
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        incident = request.GET['incident']

        serializer = IncidentSerializer(queryset, many=True)
        return Response(serializer.data)

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
