from rest_framework import serializers
from blog.models import Blog

# with the use of serializer class we can generate a json response for the blog model in the API
class BlogSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'