from django.db import models
from django import forms
# Create your models here.
class MyUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()
    descript =  models.CharField(max_length=100,null=True)
    content = models.TextField()

class testmedel(forms.Form):
    t = forms.CharField(max_length=50)