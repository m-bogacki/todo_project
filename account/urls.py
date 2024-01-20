from django.urls import path
from .views import UserListView, UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
       path('<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name="user_retrieve_update_delete"),
       path('', UserListView.as_view(), name="user_list"),
       path('create/', UserCreateView.as_view(), name="user_create")
]
