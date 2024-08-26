import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


"""
Model representing a poll question.
Contains the question text, visibility, unique code, and publication date.
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200, blank=False)
    pub_date = models.DateTimeField("date published")
    code = models.CharField(max_length=6, blank=False, unique=True)
    VISIBILITY_CHOICES=[
        ('private', 'Private'),
        ('public', 'Public')         
    ]
    visibility = models.CharField(blank=False, default='private', max_length=7, 
                                  choices=VISIBILITY_CHOICES)
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    # Determine if the poll was published recently.
    # A poll is considered recently published if it was created within the last 24 hours.
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



"""
Model representing a choice for a poll question.
Contains the choice text, vote count, and the associated question.
"""
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text