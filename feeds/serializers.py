from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post serializer for serializing into json format"""
    class Meta:
        model = Post
        fields = ('id', 'title','content','date_posted')
