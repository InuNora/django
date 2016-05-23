from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.

class QuestionManager(models.Manager):                                          
    def new():                                                              
        pass                                                            
    def popular():                                                          
        pass 

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author")
    likes = models.ManyToManyField(User)
    def __unicode__(self):              
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, null=True)
    author = models.ForeignKey(User, related_name="answer_author")
    def __unicode__(self):              # __unicode__ on Python 2
        return self.text
