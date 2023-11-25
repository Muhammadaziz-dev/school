from django.urls import path
from .views import BookListAPIView, BookDetailAPIView


urlpatterns = [
    path("", BookListAPIView.as_view()),
    path("<slug:slug>/", BookDetailAPIView.as_view()),
]