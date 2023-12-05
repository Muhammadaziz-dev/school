from django.urls import path

# from api.views import BookReviewDetailAPIView, BookReviewsApiView
from rest_framework.routers import DefaultRouter
from users.api import ProfileUpdateViewSet, LoginAPIView, RegistrationAPIView, LogoutAPIView

app_name = "api"



urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login-api'),
    path('register/', RegistrationAPIView.as_view(), name='register-api'),
    path('logout/', LogoutAPIView.as_view(), name="logout-api")
]
