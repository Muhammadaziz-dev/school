from django.urls import path
from .views import CommentsListAPIView, CommentsDetailAPIView
urlpatterns = [
    path("", CommentsListAPIView.as_view()),
    path("<int:pk>/", CommentsDetailAPIView.as_view()),
]