from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentsListSerializer, CommentsDetailSerializer
# Create your views here.

class CommentsListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer


class CommentsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsDetailSerializer

