from rest_framework import serializers
from .models import Comment

# class CommentsListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"

class CommentsListSerializer(serializers.ModelSerializer):
    blog_slug = serializers.SlugField(source='blog.slug', read_only=True)
    book_slug = serializers.SlugField(source='book.slug', read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "text", "created_at", "stars", "user", "blog", "blog_slug","book", "book_slug"]
        # extra_kwargs = {'blog': {'allow_null': True}}


class CommentsDetailSerializer(serializers.ModelSerializer):
    blog_slug = serializers.SlugField(source='blog.slug', read_only=True)
    book_slug = serializers.SlugField(source='book.slug', read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "text", "created_at", "stars", "user", "blog", "blog_slug","book", "book_slug"]


