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
    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(Userб related_name='likes')
    def __unicode__(self):              
        return self.title
    class Meta:
        db_table = 'questions'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.text
    class Meta:
        db_table = 'answers'
