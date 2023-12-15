from django.urls import path
from .api import BookListAPIView, BookDetailAPIView, BookCategoryListAPIView, BookCategoryDetailAPIView, SearchAPIView


urlpatterns = [
    path("categories/", BookCategoryListAPIView.as_view()),
    path("categories/<slug:category_slug>/", BookCategoryDetailAPIView.as_view()),
    path("", BookListAPIView.as_view()),
    path("<slug:slug>/", BookDetailAPIView.as_view()),
    
]