from rest_framework import serializers
from .models import Generic

class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        model=Generic
        fields=('name','roll','city')