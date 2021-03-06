from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework import generics, permissions

from .models import Post

class CreatePost(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    def createPost(self, serializers):
        serializers.save()
class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[permissions.IsAuthenticated]
