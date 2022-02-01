import imp
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    profile = models.ManyToManyField(Profile, related_name='user_profile')


class Car(models.Model):
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    date = models.DateField()
    

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=260, null= False, blank=False)