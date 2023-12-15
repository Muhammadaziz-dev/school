from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentsListSerializer, CommentsDetailSerializer
# from rest_framework.pagination import PageNumberPagination

# class CommentPagination(PageNumberPagination):
#     page_size = 5

class CommentsListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer
    # pagination_class = CommentPagination


class CommentsDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsDetailSerializer

