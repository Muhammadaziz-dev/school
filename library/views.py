from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer, BookDetailSerializer


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer

class BookDetailAPIView(APIView):
    def get_object(self, slug):
        return get_object_or_404(Book, slug=slug)

    def get(self, request, slug, format=None):
        book = self.get_object(slug)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
    #
    # queryset = Book.objects.all()
    # serializer_class = BookDetailSerializer