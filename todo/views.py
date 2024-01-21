from rest_framework import generics, views, response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, TaskEditSerializer

# Create your views here.


@permission_classes([IsAuthenticated])
class CreateTaskApiView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@permission_classes([IsAuthenticated])
class ListTaskApiView(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        print(self.request.user)
        return Task.objects.filter(author=self.request.user)


@permission_classes([IsAuthenticated])
class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return TaskSerializer
        else:
            return TaskEditSerializer
        

@permission_classes([IsAuthenticated])
class ToggleTaskCompletionAPIView(views.APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, pk, *args, **kwargs):
        task = Task.objects.get(pk=pk)
        task.is_complete = False if task.is_complete else True
        task.save()
        return response.Response(data=TaskSerializer(task).data)