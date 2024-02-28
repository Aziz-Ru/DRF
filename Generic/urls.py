from django.urls import path
from .views import *
urlpatterns=[
    path('',Student.as_view()),
    path('create/',CreateStudent.as_view()),
    path('retrive/<int:pk>/',RetriveStudent.as_view()),
    path('update/<int:pk>/',UpdateStudent.as_view()),
]