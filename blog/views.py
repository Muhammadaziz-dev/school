from django.shortcuts import render
from .serializers import BlogDetailSerializer, BlogListSerializer
from rest_framework import generics
from .models import Blog
# Create your views here.

class BlogListAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
