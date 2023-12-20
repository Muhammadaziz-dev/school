from django.urls import path

# from api.views import BookReviewDetailAPIView, BookReviewsApiView
from rest_framework.routers import DefaultRouter
from users.api import ProfileUpdateViewSet, LoginAPIView, RegistrationAPIView, LogoutAPIView, UserList, \
    UserDetailAPIView, UserByTokenAPIView
from library.api import SearchAPIView
from exam.api import GradeAPIView





urlpatterns = [
    path('users/register/', RegistrationAPIView.as_view(), name='user-registration'),
    path('users/login/', LoginAPIView.as_view(), name='user-login'),
    path('users/logout/', LogoutAPIView.as_view(), name='user-logout'),
    path('users/update/', ProfileUpdateViewSet.as_view({'put': 'update'}), name='profile-update'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<str:token>/', UserByTokenAPIView.as_view(), name='user-by-token'),
    path('search/', SearchAPIView.as_view(), name='library-search-api'),

    # online examples bsb chsb
    path("grade/", GradeAPIView.as_view()),

]
