from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=100,default="Default")
    email = models.EmailField(max_length=250 , unique=True)   

    def __str__(self):
        return self.name