from rest_framework import serializers
from .models import Todo
class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        #   You can also set the fields attribute to the special value '__all__' 
        #   to indicate that all fields in the model should be used
        fields=('title','body')

# The ModelSerializer class is the same as a regular Serializer class, except that:

# It will automatically generate a set of fields for you, based on the model.
# It will automatically generate validators for the serializer, such as unique_together validators.
# It includes simple default implementations of .create() and .update().
