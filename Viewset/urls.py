from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
# creating router object
router=DefaultRouter()
router.register('Path',StudenViewset,basename='student')
router.register('modelpath',StudentModelViewSet,basename='modelstudent')
# router.register('student/create/',StudenViewset,basename='student')
urlpatterns=router.urls