from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=250)
    body=serializers.CharField(max_length=250)
    
    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance old data and validated_data new data
        instance.title=validated_data.get('title',instance.title)
        instance.body=validated_data.get('body',instance.body)
        instance.save()
        return instance

#   Field-level validation
#   You can specify custom field-level validation by adding
#    .validate_<field_name> methods to your Serializer subclass.
#    Your validate_<field_name> methods should return the validated value or raise a serializers.ValidationError
    # class BlogPostSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=100)
    # content = serializers.CharField()

    # def validate_title(self, value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value

#   Object-level validation
    # To do any other validation that requires access to multiple fields,
    #  add a method called .validate() to your Serializer subclass. 
    # This method takes a single argument, which is a dictionary of field values.
    #  It should raise a serializers.ValidationError if necessary, or just return the validated values.
    
    #   def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data['start'] > data['finish']:
    #         raise serializers.ValidationError("finish must occur after start")
    #     return data