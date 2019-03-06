from rest_framework import viewsets,views
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
import json
from risk_profile.models import Hospital,School
from hazard.models import Hazard 
from .serializers import HospitalSerializer
from django.contrib.gis.db.models.functions import Distance

# Create your views here.

class HazardResourceViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request,*args,**kwargs):
        longitude = self.kwargs['long']
        latitude =self.kwargs['lat']
        hazard_title = self.kwargs['hazard']
        try:
            distance= self.kwargs['distance']
        except:
            distance=10000
        try: 
            count= self.kwargs['count']
        except:
            count=10000
        
        user_location =GEOSGeometry('POINT({} {})'.format(longitude,latitude), srid=4326)

        Hazard_object = Hazard.objects.get(title=hazard_title)
        resources = Hazard_object.hazardresources_set.all()
        print("resources",resources)
        api_json = {}
        #for resource in resources:
            #print(resource.name)
            #resouce_queryset=resource.objects.annotate(distance=Distance('location',user_location)).order_by('distance')[0:count]
            #resource_json= serialize('json',resouce_queryset)
            #api_json[resource] =resource_json
            
        return Response({"":""})

