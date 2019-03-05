from rest_framework import viewsets,views
from .models import Hospital,School
from .serializers import HospitalSerializer,SchoolSerializer
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
# Create your views here.

class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class=HospitalSerializer
    queryset=Hospital.objects.all()


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class=SchoolSerializer
    queryset=School.objects.all()
    print(GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }'))
    a=GEOSGeometry('0101000020E61000007C639A19D85B554040F64B4FCEB83B40')
    print(a.geom_type)


# class Test(viewsets.ViewSet):
#     print("Testssssssssssss")
#     def get(self,request):
#         return Response({'hello':'hello'})
