from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,BaseUserManager,AbstractUser
from django import forms
from django.utils.http import urlquote
# Create your models here.
class MyUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, default="")
    userid = models.IntegerField(unique=True, default=0)
    headlink = models.CharField(max_length=50, default="ssdasdasda")
    USERNAME_FIELD = 'username'

class Blog(models.Model):
    blog_id = models.CharField(primary_key=True,unique=True,max_length=100)
    title = models.CharField(max_length=50)
    link = models.URLField()
    descript =  models.CharField(max_length=100,null=True)
    content = models.TextField()
    

class Comment(models.Model):
    comment_id = models.CharField(primary_key=True,unique=True,max_length=100)
    userid = models.IntegerField(unique=True)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    username = models.CharField(max_length=20)
    headimg = models.CharField(max_length=50)
    test = models.CharField(max_length=100)
    
class Reply(models.Model):
    reply_id = models.CharField(primary_key=True,unique=True,max_length=100)
    to_userId = models.IntegerField(unique=True, default=0)
    username = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    headimg = models.CharField(max_length=50)
    to = models.CharField(max_length=20)


class testmedel(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()