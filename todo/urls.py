from django.urls import path
from .views import RetrieveUpdateDestroyTaskView, ListTaskApiView, CreateTaskApiView, ToggleTaskCompletionAPIView

urlpatterns = [
    path('<int:pk>', RetrieveUpdateDestroyTaskView.as_view(),name='task_delete_get_update'),
    path('<int:pk>/toggle-complete', ToggleTaskCompletionAPIView.as_view(), name='task_complete'),
    path('', ListTaskApiView.as_view()),
    path('create/', CreateTaskApiView.as_view(), name="create_task")
]