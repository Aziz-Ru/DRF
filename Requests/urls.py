from django.urls import path
from .views import *
urlpatterns=[
    path('request/',Request_View.as_view()),
    path('response/',Response_View.as_view()),
    
]