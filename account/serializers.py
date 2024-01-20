from rest_framework.serializers import ModelSerializer, CharField
from .models import User

class UserListSerializer(ModelSerializer):
    
    class Meta:
        model = User
        exclude = ["user_permissions", "groups", "password", "is_staff", "first_name", "is_superuser", "last_login"]

class UserCreateSerializer(ModelSerializer):
    
    class Meta:
        model = User
        exclude = ["user_permissions", "groups"]

