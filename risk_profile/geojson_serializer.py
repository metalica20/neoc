from django.core import serializers

GeoJSONSerializer = serializers.get_serializer("geojson")

class Serializer(GeoJSONSerializer):
    def get_dump_object(self, obj):
        data = super(Serializer, self).get_dump_object(obj)
        print(data)
        # Extend to your taste
        data['properties'].update({'title':obj.title, 'description': obj.description, 'ward': obj.ward.title})
        data.update({'geometry':{"type": "Point", "coordinates":[obj.point.x,obj.point.y]}})
        return data
