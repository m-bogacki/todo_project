from django.urls import path
from .views import RetrieveUpdateDestroyTaskView, CreateTaskApiView

urlpatterns = [
    path('', RetrieveUpdateDestroyTaskView.as_view()),
    path('create/', CreateTaskApiView.as_view(), name="create-task")
]