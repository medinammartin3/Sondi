from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Extends Django's AbstractUser model to create a custom user model 
with a unique email field.
"""
class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)

    # Display the username when this model is referenced as a foreign key
    def __str__(self):
        return self.username