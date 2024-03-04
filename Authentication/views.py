from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def list(self, request, *args, **kwargs):
        return Response({'message':"Helllo How areyou"})
    
