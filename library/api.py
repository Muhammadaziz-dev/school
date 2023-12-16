from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from comments.models import Comment
from django import forms
from comments.serializers import CommentsDetailSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, generics
from rest_framework.generics import ListAPIView
from .models import Book, Category
from .serializers import BookSerializer, BookDetailSerializer, BookCategorySerializer, BookCategoryDetailSerializer


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class SearchAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            self.queryset = Book.objects.filter(name__icontains=query)
        return super().get(request, *args, **kwargs)


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


class BookCategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = BookCategorySerializer
    lookup_field = "category_slug"

class BookCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = BookCategoryDetailSerializer
    lookup_field = "category_slug"


    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)