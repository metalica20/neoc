import json
from rest_framework import renderers


class GeoJSONRenderer(renderers.BaseRenderer):
    # TODO: media type?
    media_type = 'application/json'
    format = 'geojson'
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return json.dumps(data['results'])
