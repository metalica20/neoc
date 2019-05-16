from django.core import serializers

GeoJSONSerializer = serializers.get_serializer("geojson")

class Serializer(GeoJSONSerializer):
    def get_dump_object(self, obj):
        data = super(Serializer, self).get_dump_object(obj)
        # print(data)
        print(obj.title)
        # Extend to your taste 'ward': obj.ward.title
        data['properties'].update({'title':obj.title,'description': obj.description,})
        data.update({'geometry':{"type": "Point", "coordinates":[obj.point.x,obj.point.y]}})
        return data
