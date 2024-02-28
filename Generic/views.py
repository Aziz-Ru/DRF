from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from .serializers import GenericSerializer
from .models import Generic

class Student(GenericAPIView,ListModelMixin):
    queryset=Generic.objects.all()
    serializer_class=GenericSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
     
class CreateStudent(GenericAPIView,CreateModelMixin):
    queryset=Generic.objects.all()
    serializer_class=GenericSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RetriveStudent(GenericAPIView,RetrieveModelMixin):
    #url name must be /retrive(orsomething)/<int:pk>/ pk musthere
    queryset=Generic.objects.all()
    serializer_class=GenericSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class UpdateStudent(GenericAPIView,UpdateModelMixin):
    #url name must be /retrive(orsomething)/<int:pk>/ pk musthere
    queryset=Generic.objects.all()
    serializer_class=GenericSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    