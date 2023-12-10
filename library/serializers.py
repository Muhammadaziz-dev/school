from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'id', 'slug', "cover_image")

class BookDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.category_name")
    class Meta:
        model = Book
        fields = "__all__"