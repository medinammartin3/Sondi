from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Extends Django's AbstractUser model to create a custom user model 
with a unique email field.
"""
class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    # Questions where the user has voted
        # Using question codes to store the questions voted by the user 
        # instead of IDs to avoid issues with duplicate IDs if a question 
        # is deleted and a new one is created with the same ID.
        # This reduces the chance of voting issues due to ID reuse.
        # This is also possible with question codes, but less probable due to
        # the algorithm used for code generation.
    voted_questions =  models.JSONField(default=dict) # Initialize with a new dictionary instance
                                                      # Structure :
                                                      #{
                                                      #   "voted_questions": [
                                                      #      "code1",
                                                      #      "code2",
                                                      #      "code3",
                                                      #        ...
                                                      #   ]
                                                      #}
                                          

    # Display the username when this model is referenced as a foreign key
    def __str__(self):
        return self.username