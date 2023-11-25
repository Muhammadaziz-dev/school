from django.urls import path
from .views import BlogDetailAPIView, BlogListAPIView

urlpatterns = [
    path("", BlogListAPIView.as_view()),
    path("<int:pk>/", BlogDetailAPIView.as_view()),
]