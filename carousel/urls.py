from django.urls import path
from .api import CarouselListAPIView
urlpatterns = [
    path('', CarouselListAPIView.as_view()),
]