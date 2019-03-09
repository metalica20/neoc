from rest_framework import viewsets,views
from .models import Hospital,School,MarketCenter,LayerTable,Airport,Bridge,Policestation,Education
from .serializers import HospitalSerializer,SchoolSerializer,LayerTableSerializer
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
import json
# Create your views here.

class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class=HospitalSerializer
    queryset=Hospital.objects.all()


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class=SchoolSerializer
    queryset=School.objects.all()
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
