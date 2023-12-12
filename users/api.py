from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets, generics

from .serializers import UserUpdateSerializer, UserRegistrationSerializer, \
    UserLoginSerializer, UserSerializer

from users.forms import UserCreateForm, UserUpdateForm
from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse

from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from .tasks import send_email

from .models import CustomUser
from rest_framework.authtoken.models import Token


class RegistrationAPIView(APIView):
    def post(self, request):
        create_form = UserCreateForm(data=request.data)

        if create_form.is_valid():
            user = create_form.save()

            token, created = Token.objects.get_or_create(user=user)

            # ... rest of your code

            return Response({"message": "User registered successfully", "token": token.key},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Invalid form data", "errors": create_form.errors},
                            status=status.HTTP_400_BAD_REQUEST)




class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']

            user = authenticate(username=phone, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)

            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid crediantls"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


# class ProfileUpdateViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserUpdateSerializer
#     queryset = CustomUser.objects.all()
#
#     def get_queryset(self):
#         return User.objects.filter(id=self.request.user.id)
#
#     def get_serializer_class(self):
#         return UserUpdateForm

class ProfileUpdateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def __init__(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            super().__init__(*args, **kwargs)
            return

        super().__init__(*args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        create_form = UserCreateForm(data=request.data)

        if create_form.is_valid():
            user = create_form.save()

            token, created = Token.objects.get_or_create(user=user)

            # ... rest of your code

            return Response({"message": "User registered successfully", "token": token.key},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Invalid form data", "errors": create_form.errors},
                            status=status.HTTP_400_BAD_REQUEST)


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
            serializer = UserSerializer(user)
            return Response({
                'user_id': user.id,
                'username': user.username,
                'user_data': serializer.data,
            })
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, token):
        try:
            user = CustomUser.objects.get(auth_token=token)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update specific fields if provided in the request
        for field in ('username', 'email', 'phone_number', 'first_name', 'last_name'):
            if field in request.data:
                setattr(user, field, request.data[field])

        try:
            user.full_clean()  # Validate the user instance
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)