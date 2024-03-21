
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

route=DefaultRouter()
route.register('auth',Account_ViewSet,basename='auth')
urlpatterns=route.urls