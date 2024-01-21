from rest_framework.serializers import ModelSerializer, CharField
from .models import User

class UserListSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "email"]

class UserCreateSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ["email", "password"]
    

