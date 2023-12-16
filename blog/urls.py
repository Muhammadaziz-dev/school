from django.urls import path
from .api import BlogDetailAPIView, BlogListAPIView,AllBlogAPIView, SearchAPIView

urlpatterns = [
    path("", BlogListAPIView.as_view()),
    path("all/", AllBlogAPIView.as_view()),
    path('search/', SearchAPIView.as_view(), name='library-search-api'),
    path("<slug:slug>/", BlogDetailAPIView.as_view()),
]