
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('Authentication.urls')),
    path('r/', include('Requests.urls')),
    # path('serializer/', include('Serializer.urls')),
    path('g/', include('Generic.urls')),
    path('token/', include('TokenAuth.urls')),
    path('v/', include('Viewset.urls')),
]
