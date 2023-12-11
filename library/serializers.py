from rest_framework import serializers
from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    category_slug = serializers.CharField(source="category.category_slug")
    category_name = serializers.CharField(source="category.category_name")
    class Meta:
        model = Book
        fields = ('name', 'id', 'slug', "cover_image", "category_slug", "category_name")

class BookDetailSerializer(serializers.ModelSerializer):
    category_slug = serializers.CharField(source="category.category_slug")
    category_name = serializers.CharField(source="category.category_name")
    class Meta:
        model = Book
        fields =  ('name', 'id', 'slug', "cover_image", "category_slug", "category_name", "author", "isbn", "description", "book_file")



class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'category_name', "category_slug")

class BookCategoryDetailSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True, read_only=True)
    books = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_slug','books')

    def get_books(self, obj):
        books = Book.objects.filter(category=obj)
        serializer = BookSerializer(books, many=True)
        return serializer.data
