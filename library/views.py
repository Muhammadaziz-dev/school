from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer