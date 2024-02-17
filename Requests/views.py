from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import Student_Serializer
from .renderers import Error_Renderer
class Request_View(APIView):
    def get(self,request):
        # print(request.data)
        # print(request.method)
        # print(request.content_type)
        # print(request.query_params)
        return Response({'Message':request.data.get('message'),
                         'params':request.query_params,
                         'method':request.method,
                         'content_type':request.content_type,
                         },
                         status=status.HTTP_200_OK)

# Response(data, status=None, template_name=None, headers=None, content_type=None)
class Response_View(APIView):
    # renderer_classes=[Error_Renderer]
    def get(self,request):
        student=Student.objects.all()
        serializer=Student_Serializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK,)
    def post(self,request):
        serializer=Student_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
# API policy attributes
# renderer_classes
# parser_classes
# authentication_classes
# throttle_classes
# permission_classes
# content_negotiation_class
    
# class StudentSet_View(viewsets.ViewSet):
#     def list(self,request):
#         student=Student.objects.all()
#         serializer=Student_Serializer(student,many=True)
#         return Response(serializer.data)
#     def retrieve(self,request,pk=None):
#         if id is not None:
#             student=Student.objects.get(id=pk)
#             serializer=Student_Serializer(student)
#             return Response(serializer.data)
    
#     def create(self,request):
#         serializer=Student_Serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'message':'Created Successfully'})
    
#     def update(self,request,pk):
#         student=Student.objects.all(pk=pk)
#         serializer=Student_Serializer(student,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'message':'Updated Successfully'})


