from rest_framework import viewsets,views
from .models import Hospital,School,MarketCenter,LayerTable
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
        serializers=serialize('geojson',Hospital.objects.all(),geometry_field='location',fields=('pk','fid','name','district'))
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


class LayerViewset(viewsets.ModelViewSet):
    serializer_class=LayerTableSerializer
    queryset=LayerTable.objects.all()
