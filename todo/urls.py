from django.urls import path
from .views import RetrieveUpdateDestroyTaskView, ListTaskApiView, CreateTaskApiView

urlpatterns = [
    path('<int:pk>', RetrieveUpdateDestroyTaskView.as_view()),
    path('', ListTaskApiView.as_view()),
    path('create/', CreateTaskApiView.as_view(), name="create-task")
]