from rest_framework import serializers
from .models import Comment

class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "user", "blog", "book")

class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"