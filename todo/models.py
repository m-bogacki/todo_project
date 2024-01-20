from django.db import models
from account.models import User

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    due_date = models.DateField(blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)