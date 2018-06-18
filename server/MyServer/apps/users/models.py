from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    userId = models.AutoField(unique=True, default=0,primary_key=True)

class UserInfo(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    userId = models.IntegerField(unique=True, primary_key=True)
    iconUrl = models.URLField(default="/media/head.jpg")
    newlyTime = models.DateField(auto_now=True)

class UserMessage(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='FromUser')
    toUser = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='ToUser')
    msgType = models.CharField(max_length=20, choices=(('LE', 'letter'), ('INT','interest')))
    time = models.DateTimeField(auto_now=True)
    isRead = models.BooleanField(default=False)
    content = models.CharField(max_length=200, null=True)

class SystemMessage(models.Model):
    toUser = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    isRead = models.BooleanField(default=False)

