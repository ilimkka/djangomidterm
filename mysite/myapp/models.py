import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
 
# Remember the three-step guide to making model changes:
    # Change your models (in models.py).
    # Run python mysite/manage.py makemigrations to create migrations for those changes
    # Run python mysite/manage.py migrate to apply those changes to the database.

class Question(models.Model):
    nickname = models.CharField(max_length=15, default='anonim')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_set', default=1)
    nickname = models.CharField(max_length=15, default='anonim')
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.answer_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text