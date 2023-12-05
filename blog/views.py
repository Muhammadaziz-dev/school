from django.shortcuts import render
from .serializers import BlogDetailSerializer, BlogListSerializer
from rest_framework import generics
from .models import Blog
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class BlogListAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

class BlogDetailAPIView(APIView):
    def get_object(self, slug):
        return get_object_or_404(Blog, slug=slug)

    def get(self, request, slug, format=None):
        blog = self.get_object(slug)
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data)