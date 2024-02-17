from rest_framework import renderers
import json

class Error_Renderer(renderers.JSONRenderer):
    #Renders the request data into JSON, using utf-8 encoding.
    charset='utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response=''
        #ErrorDetail in serializer.errors
        if 'ErrorDetail' in str(data):
            response=json.dumps({'errors':data})
        else:
            response=json.dumps(data)
        return response
