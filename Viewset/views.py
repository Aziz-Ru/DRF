from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .renders import JSONRenderers
from .serializers import StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudenViewset(viewsets.ViewSet):
    # permission_classes=[IsAuthenticated]
    renderer_classes=[JSONRenderers]
    def list(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        try:
            student=Student.objects.get(id=pk)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        except:
            return Response({'message':'Not Found'})
        
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':"Created account successfully"})
    
    def update(self,request,pk):
        try:
            student=Student.objects.get(pk=pk)
            serializer=StudentSerializer(student,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message':"Updated account successfully"})
        except:
            return Response({'message':'Not Found To Update'})
        
    def partial_update(self,request,pk):
        try:
            student=Student.objects.get(pk=pk)
            serializer=StudentSerializer(student,data=request.data,partial=True)
            serializer.save()
            return Response({'message':"Updated account successfully"})
        except:
            return Response({'message':'Not Found'})
    
    def destroy(self,request,pk):
        try:
            student=Student.objects.get(id=pk)
            student.delete()
            return Response({'message':"Deleted account successfully"})
        except:
            return Response({'message':'Not Found'})




