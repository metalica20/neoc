from rest_framework import viewsets,views
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from rest_framework import viewsets,views
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from rest_framework.renderers import JSONRenderer
import json
from risk_profile.models import Hospital,School
from .serializers import ModelSerializer
from hazard.models import Hazard, HazardResources
from .serializers import HospitalSerializer, HazardResourceSerializer
from django.contrib.gis.db.models.functions import Distance
from django.apps import apps
import io
from rest_framework.parsers import JSONParser
from django.contrib.gis.measure import D
from django.views.generic import TemplateView
from risk_profile.models import LayerTable
from incident.models import Incident
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.


class HazardResourceViewSetView(viewsets.ModelViewSet):
    serializer_class = HazardResourceSerializer
    queryset = HazardResources.objects.all().select_related('hazard', 'resource')

    def get_queryset(self):
        incident = int(self.request.GET.get('incident'))
        incident_obj = get_object_or_404(Incident, id=incident)
        hazard = incident_obj.hazard
        return self.queryset.filter(hazard=hazard)

    def get_serializer_context(self):
        incident = int(self.request.GET.get('incident'))
        count = self.request.GET.get('count', 30)

        max_distance = int(self.request.GET.get('max_distance', 1000))
        incident_obj = get_object_or_404(Incident, id=incident)
        lat = incident_obj.point.y
        longitude = incident_obj.point.x
        user_location = GEOSGeometry('POINT({} {})'.format(longitude, lat), srid=4326)
        return {'count': count, 'max_distance': max_distance, 'user_location': user_location}

# class HazardResourceViewSetView(views.APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, *args, **kwargs):
#         incident = int(request.GET.get('incident'))
#         count = request.GET.get('count')
#         max_distance = int(request.GET.get('max_distance'))
#         try:
#             incident_obj = Incident.objects.get(id=incident)
#         except:
#             return JsonResponse({'error': 'Incident object doest not exist of requested id.'})
#         lat = incident_obj.point.y
#         longitude = incident_obj.point.x
#         hazard_title = incident_obj.hazard.title
#
#         user_location = GEOSGeometry('POINT({} {})'.format(longitude, lat), srid=4326)
#         api_json = {}
#         resource_array = []
#         if (hazard_title == 'Flood'):
#             resource_array.extend(['Hospital', 'School', 'Policestation', 'Bridge'])
#         elif (hazard_title == 'Landslide'):
#             resource_array.extend(['Policestation', 'Hospital', 'School'])
#         elif (hazard_title == 'Fire'):
#             resource_array.extend(['Policestation', 'Hospital', 'School', 'MarketCenter'])
#         elif (hazard_title == 'Earthquake'):
#             resource_array.extend(['Policestation', 'Hospital', 'School'])
#
#         resource_object = []
#         for resource in resource_array:
#             model_x = apps.get_model('risk_profile', resource)
#             resource_queryset = model_x.objects \
#                                     .filter(location__distance_lte=(user_location, D(km=max_distance))) \
#                                     .annotate(distance=Distance('location', user_location)) \
#                                     .order_by('distance')[0:int(count)]
#             resource_json = ModelSerializer(resource_queryset, many=True)
#             json = JSONRenderer().render(resource_json.data)
#             stream = io.BytesIO(json)
#             data = JSONParser().parse(stream)
#             api_json[resource] = {'resources': data}
#
#         return Response(api_json)


class HazardResourceViewSet(views.APIView):
    permission_classes=[]

    def get(self,request,*args,**kwargs):
        longitude = self.kwargs['long']
        latitude =self.kwargs['lat']
        hazard_title = self.kwargs['hazard']
        try:
            distance_parm= self.kwargs['distance']
        except:
            distance_parm=5000
        try:
            count= int(self.kwargs['count'])
        except:
            count=20

        user_location =GEOSGeometry('POINT({} {})'.format(longitude,latitude), srid=4326)

        #Hazard_object = Hazard.objects.get(title=hazard_title)
        #Hresources = Hazard_object.hazardresources_set.all()
        api_json = {}

        if(hazard_title=='flood'):
            resource_array=['Hospital','School','Policestation','Bridge']
        elif (hazard_title=='landslide'):
            resource_array=['Policestation','Hospital','School']
        elif (hazard_title=='fire'):
            resource_array=['Policestation','Hospital','School','MarketCenter']
        elif (hazard_title=='earthquake'):
            resource_array=['Policestation','Hospital','School']



        resource_object=[]
        print(distance_parm)
        for resource in resource_array:
            model_x= apps.get_model('risk_profile', resource)
            print("model_x",model_x)
            resource_queryset=model_x.objects \
            .filter(location__distance_lte=(user_location,D(km=distance_parm))) \
            .annotate(distance=Distance('location',user_location)) \
            .order_by('distance')[0:count]
            print(resource_queryset)
            resource_json= HospitalSerializer(resource_queryset,many=True)
            json = JSONRenderer().render(resource_json.data)
            stream = io.BytesIO(json)
            data = JSONParser().parse(stream)
            api_json[resource] =data

        return Response(api_json)



# HTML View

class MapPage(TemplateView):
    template_name= 'mapPage.html'
    def get(self, request, *args, **kwargs):
        hazard= LayerTable.objects.filter(layer_cat='hazard')
        vul= LayerTable.objects.filter(layer_cat='vulnerability')
        resource= LayerTable.objects.filter(layer_cat='resource')
        exposure= LayerTable.objects.filter(layer_cat='exposure')






        return render(request, 'map.html', {'hazards': hazard,'resources':resource,'vulnerabilities':vul,'exposures':exposure})
