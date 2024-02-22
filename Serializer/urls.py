from django.urls import path
from .views import *

urlpatterns =[
    path('todo/',TodoView.as_view()),
    path('model/',TodoModelView.as_view()),
    path('base/',BaseSerializerView.as_view()),
]