from rest_framework import generics
from .models import Task
from .serializers import TaskCreateSerializer, TaskEditSerializer

# Create your views here.


class CreateTaskApiView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer