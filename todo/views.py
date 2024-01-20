from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskEditSerializer

# Create your views here.


class CreateTaskApiView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer
    
class ListTaskApiView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return TaskSerializer
        else:
            return TaskEditSerializer