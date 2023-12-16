from django.urls import path
from .api import CommentsListAPIView, CommentsDetailAPIView, SearchAPIView

urlpatterns = [
    path("", CommentsListAPIView.as_view()),
    path('search/', SearchAPIView.as_view(), name='library-search-api'),
    path("<int:pk>/", CommentsDetailAPIView.as_view()),
]