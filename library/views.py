from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from comments.models import Comment
from comments.serializers import CommentsDetailSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer

class BookPagination(PageNumberPagination):
    page_size = 20

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = "slug"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        comments = Comment.objects.filter(book__id=instance.id)
        comment_serializer = CommentsDetailSerializer(comments, many=True)
        data = serializer.data
        data['comments'] = comment_serializer.data
        return Response(data)