from django.shortcuts import render
from .serializers import BlogDetailSerializer, BlogListSerializer, AllBlogsSerializer
from rest_framework import generics, filters
from .models import Blog
from rest_framework.response import Response
from comments.models import Comment
from django import forms
from comments.serializers import CommentsDetailSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class SearchAPIView(ListAPIView):
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'title', 'created_at']


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


class AllBlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = AllBlogsSerializer
