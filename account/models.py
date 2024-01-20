from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password

# Create your models here.



class User(AbstractUser):
    
    def create(self, *args, **kwargs):
        self.date_joined = timezone.now()
        self.password = make_password(self.password)
        super(User, self).create(*args,**kwargs)
    

