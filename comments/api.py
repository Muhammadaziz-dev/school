from django.shortcuts import render
from rest_framework import generics, filters
from .models import Comment
from .serializers import CommentsListSerializer, CommentsDetailSerializer
# from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django import forms

# class CommentPagination(PageNumberPagination):
#     page_size = 5


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class SearchAPIView(ListAPIView):
    serializer_class = CommentsListSerializer
    queryset = Comment.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'text', 'created_at', 'user']


class CommentsListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer
    # pagination_class = CommentPagination


class CommentsDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsDetailSerializer

