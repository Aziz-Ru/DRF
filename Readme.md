# Django REST Framework

## REST Architecture

Representational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other.

## Request

REST framework's Request class extends the standard HttpRequest, adding support for REST framework's flexible request parsing(one format to another format ) and request authentication.Request objects provide flexible request parsing that allows you to treat requests with JSON data or other media types in the same way that you would normally deal with form data.

### request.data

It returns the parsed content of the request body. This is similar to the standard request.POST

```
const response = await fetch('https://jsonplaceholder.typicode.com/posts,{
    method:'POST'
    body:'JSON.stringify({
        title:'Jsonplaceholder'
        body:'Open API'
    }),
    headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },


})



```

Here body data you will get in request.data[]

### request.query_params

request.query_params is a more correctly named synonym for request.GET.IN this url 'http://127.0.0.1:8000/r/request/?id=1&&name=aziz' id and name is query params

### request.user

request.user typically returns an instance of django.contrib.auth.models.User, although the behavior depends on the authentication policy being used.If the request is unauthenticated the default value of request.user is an instance of django.contrib.auth.models.AnonymousUser.

###

request.auth returns any additional authentication context.The exact behavior of request.auth depends on the authentication policy being used, but it may typically be an instance of the token that the request was authenticated against.

#### request.content_type

request.content_type, returns a string object representing the media type of the HTTP request's body, or an empty string if no media type was provided.

## Response

The Response class subclasses Django's SimpleTemplateResponse.There's no requirement for you to use the Response class, you can also return regular HttpResponse or StreamingHttpResponse objects from your views if required. Using the Response class simply provides a nicer interface for returning content-negotiated Web API responses, that can be rendered to multiple formats.

```
Signature: Response(data, status=None, template_name=None, headers=None, content_type=None)
```

## Views

REST framework provides an APIView class, which subclasses Django's View class.REST framework also allows you to work with regular function based views.The core of this functionality is the api_view decorator, which takes a list of HTTP methods that your view should respond to.

```
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view(['GET','POST'])
def FunbasedView():
    return Response({"message": "Hello, world!"})

class ClassBasedView(APIView):

    def get(self,request):
        return Response({"message": "Hello, world!"})


```

## API policy attributes

```
renderer_classes
parser_classes
authentication_classes
throttle_classes
permission_classes
```

## GenericAPIView

This class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.The following attributes control the basic view behavior.

queryset:The queryset that should be used for returning objects from this view.

serializer_class: The serializer class that should be used for validating and deserializing input, and for serializing output.

lookup_field:The model field that should be used for performing object lookup of individual model instances. Defaults to 'pk'.

get_queryset(self):
Returns the queryset that should be used for list views, and that should be used as the base for lookups in detail views

```
def get_queryset(self):
    user = self.request.user
    return user.accounts.all()
```

## ViewSets

A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create()

```
class UserViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
```

```
from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
```

## ModelViewSet

The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the behavior of the various mixin classes.

```
class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
```

## Router


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
