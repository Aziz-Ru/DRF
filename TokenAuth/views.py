# include rest_framework.authtoken in your INSTALLED_APPS setting
# Make sure to run manage.py migrate after changing your settings
# The rest_framework.authtoken app provides Django database migrations.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import AccountSerializer
from rest_framework.authtoken.models import Token

class Account_ViewSet(viewsets.ViewSet):

    def create(self,request):
        serializer=AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        token=Token.objects.create()
        return Response({'message':"Created account successfully"})
    

