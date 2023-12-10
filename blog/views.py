from django.shortcuts import render
from .serializers import BlogDetailSerializer, BlogListSerializer
from rest_framework import generics
from .models import Blog
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from comments.models import Comment
from comments.serializers import CommentsDetailSerializer
from rest_framework.pagination import PageNumberPagination


class BlogPagination(PageNumberPagination):
    page_size = 20

class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    pagination_class = BlogPagination

class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'  # Qo'shilgan qismi

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        comments = Comment.objects.filter(blog__id=instance.id)
        comment_serializer = CommentsDetailSerializer(comments, many=True)
        data = serializer.data
        data['comments'] = comment_serializer.data
        return Response(data)


