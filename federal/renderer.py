import json
from rest_framework import renderers


class GeoJSONRenderer(renderers.BaseRenderer):
    media_type = 'application/vnd.geo+json'
    format = 'geojson'
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return json.dumps(data['results'])
