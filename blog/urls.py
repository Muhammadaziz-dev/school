from django.urls import path
from .views import BlogDetailAPIView, BlogListAPIView,AllBlogAPIView

urlpatterns = [
    path("", BlogListAPIView.as_view()),
    path("all/", AllBlogAPIView.as_view()),
    path("<slug:slug>/", BlogDetailAPIView.as_view()),
]