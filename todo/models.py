from django.db import models
from account.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True,null=True)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)