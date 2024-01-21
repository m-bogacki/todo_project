from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from drf_spectacular.utils import extend_schema
from .models import User
from .serializers import UserListSerializer, UserCreateSerializer
from django.contrib.auth.hashers import make_password

@permission_classes([IsAuthenticated])
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

@permission_classes([AllowAny])
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password
        return super().perform_create(serializer)
    
@permission_classes([IsAuthenticated])
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
        