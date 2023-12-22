from django.urls import path
from .api import GradeAPIView


urlpatterns = [
    path('',GradeAPIView.as_view()),
]