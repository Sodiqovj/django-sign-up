from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    pass

class My(models.Model):
    name = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name