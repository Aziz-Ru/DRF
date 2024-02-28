
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('Requests.urls')),
    # path('serializer/', include('Serializer.urls')),
    # path('generic/', include('Generic.urls')),
    path('viewset/', include('Viewset.urls')),
]
