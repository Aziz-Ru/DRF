from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
# creating router object
router=DefaultRouter()
router.register('user',UserViewset,basename='user')

urlpatterns=router.urls