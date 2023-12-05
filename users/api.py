from django.contrib.auth.models import User
from django.http import request
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, generics


from .serializers import UserUpdateSerializer, UserRegistrationSerializer, \
UserLoginSerializer, UserSerializer
from users.forms import UserUpdateForm
from users.forms import UserCreateForm
from django.contrib.auth import logout

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser
from rest_framework.authtoken.models import Token


class RegistrationAPIView(APIView):
    def post(self, request):
        create_form = UserCreateForm(data=request.data)

        if create_form.is_valid():
            user = create_form.save()
            token, created = Token.objects.get_or_create(user=user)  # Create or retrieve the token
            return Response({"message": "User registered successfully", "token": token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(create_form.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        login_form = AuthenticationForm(data=request.data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)  # Create or retrieve the token
            return Response({"message": "Login successful", "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class ProfileUpdateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        return UserUpdateForm


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(APIView):
    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserByTokenAPIView(APIView):
    def get(self, request, token):
        try:
            user = CustomUser.objects.get(auth_token=token)
            serializer = UserSerializer(user)  # Serialize the user data
            return Response(

                serializer.data,  # Include the serialized user data in the response
            )
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

    def patch(self, request, token):
        try:
            user = CustomUser.objects.get(auth_token=token)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        # Update specific fields if provided in the request
        for field in ('username', 'email', 'first_name', 'last_name'):
                    setattr(user, field, request.data[field])

        user.save()

        # Serialize the updated user data
        serializer = UserSerializer(user)
        return Response(serializer.data)