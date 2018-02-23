from django.db import models
from django import forms
# Create your models here.
class MyUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Blog(models.Model):
    blog_id = models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=50)
    link = models.URLField()
    descript =  models.CharField(max_length=100,null=True)
    content = models.TextField()

class Commemt(models.Model):
    comment_id = models.OneToOneField(Blog, primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    headimg = models.CharField(max_length=50)
    
class Reply(models.Model):
    reply_id = models.OneToOneField(Commemt,primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    headimg = models.CharField(max_length=50)
    to = models.CharField(max_length=20)


class testmedel(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()