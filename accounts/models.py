# api-small-business/accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    """This is a custom user class that extends from 
    AbstractUser"""
    pass