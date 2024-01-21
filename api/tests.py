from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from account.models import User
from todo.models import Task
from rest_framework.test import APITestCase, force_authenticate
from rest_framework_simplejwt.tokens import AccessToken



class TodoAPITests(APITestCase):
    def setUp(self):
        # Twórz użytkownika do testów
        self.user = User.objects.create(email='test@wp.pl', password='testpassword')


    
    def test_create_user(self):
        """
        Ensure we can create a new account object.
        """
        
        
        
        url = reverse('user_create')
        data = {'email': 'test@example.com', 'password': "string"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(email="test@example.com").email, 'test@example.com')
        
    def test_create_task(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('create_task')
        data = {
        "title": "string",
        "description": "string",
        "is_complete": False,
        "due_date": "2024-01-21T21:34:25.127Z"
        }
        
        access_token = AccessToken.for_user(self.user)

        # "Wymuszanie" autentykacji z użyciem JWT
        self.client.force_authenticate(user=self.user, token=str(access_token))
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, "string")
        
    def test_toggle_task_completion(self):

        Task.objects.create(
        title= "string",
        description= "string",
        is_complete= True,
        due_date= "2024-01-21T21:34:25.127Z",
        author=self.user
        )

        access_token = AccessToken.for_user(self.user)

        # "Wymuszanie" autentykacji z użyciem JWT
        self.client.force_authenticate(user=self.user, token=str(access_token))

        url = reverse('task_complete', kwargs={"pk": 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().is_complete, False)
        
    def test_task_delete(self):

        Task.objects.create(
        title= "string",
        description= "string",
        is_complete= True,
        due_date= "2024-01-21T21:34:25.127Z",
        author=self.user
        )

        access_token = AccessToken.for_user(self.user)

        # "Wymuszanie" autentykacji z użyciem JWT
        self.client.force_authenticate(user=self.user, token=str(access_token))
        url = reverse('task_delete_get_update', kwargs={"pk": 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)