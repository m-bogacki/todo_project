from rest_framework import serializers
from .models import Task
from account.serializers import UserListSerializer

class TaskCreateSerializer(serializers.ModelSerializer):
    author = UserListSerializer()

    class Meta:
        model = Task
        fields = "__all__"

class TaskEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ["author"]