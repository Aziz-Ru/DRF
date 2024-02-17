# Django REST Framework

Representational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other.

## Request

REST framework's Request class extends the standard HttpRequest, adding support for REST framework's flexible request parsing and request authentication.Request objects provide flexible request parsing that allows you to treat requests with JSON data or other media types in the same way that you would normally deal with form data.

#### request.data

it returns the parsed content of the request body.

#### request.user

request.user typically returns an instance of django.contrib.auth.models.User, although the behavior depends on the authentication policy being used.If the request is unauthenticated the default value of request.user is an instance of django.contrib.auth.models.AnonymousUser.

#### request.content_type

request.content_type, returns a string object representing the media type of the HTTP request's body, or an empty string if no media type was provided.

#### Renderer classes

REST framework includes a number of built in Renderer classes, that allow you to return responses with various media types. There is also support for defining your own custom renderers, which gives you the flexibility to design your own media types.

#### Default Renderer classes

ADD in setting

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
```

#### Custom Renderer classes

```
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

```

## Serializers

Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
