from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import TodoSerializer
from .models import Todo


#   When deserializing data, you always need to call is_valid()
#   before attempting to access the validated data, or save an 
#   object instance. If any validation errors occur, the .errors property 
#   will contain a dictionary representing the resulting error messages.
#   The non_field_errors key may also be present, and will list any general validation errors.
#   The name of the non_field_errors key may be customized using the NON_FIELD_ERRORS_KEY REST framework setting
#   The .is_valid() method takes an optional raise_exception flag that will cause it to raise a serializers.ValidationError exception if there are validation errors.

class TodoView(APIView):
    def get(self,request):
        todos=Todo.objects.get(id=1)
        #   Similarly if a nested representation should be a list of items,
        #   you should pass the many=True flag to the nested serializer.
        return Response({'title':todos.title,'body':todos.body})
    def post(self,request):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.query_params.get('id')
        try:
            todo=Todo.objects.get(id=id)
            serializer=TodoSerializer(todo,request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":'Data is Updated Successfully'})
            return Response(serializer.errors)
        except:
            return Response({'message':'Not Found'})
    
    def delete(self, request):
    
        id = request.query_params.get('id')

        try:
            todo = get_object_or_404(Todo, pk=id)
            todo.delete()
            return Response({'message': "Successfully deleted"})
        except Todo.DoesNotExist:
            return Response({'message': "Todo not found"}, status=status.HTTP_404_NOT_FOUND)