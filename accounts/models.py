from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser) :
    age = models.PositiveIntegerField(null=True,blank=True)


    

