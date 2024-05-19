from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {
            'code': 200,
            'data': data
        }

        return super().render(response_data, accepted_media_type, renderer_context)
