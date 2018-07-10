from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    userId = models.AutoField(unique=True, primary_key=True)

class UserInfo(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    userId = models.OneToOneField(MyUser, primary_key=True,on_delete=models.CASCADE, related_name='UserInfo', db_column='userId')
    iconUrl = models.URLField(default="/media/head.jpg")
    newlyTime = models.DateField(auto_now_add=True)

class UserMessage(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='FromUser', db_column='user')
    toUser = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='ToUser', db_column='toUser')
    msgType = models.CharField(max_length=20, null=False, blank=False,choices=(('LE', 'letter'), ('INT','interest')))
    time = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)
    content = models.CharField(max_length=200, null=True)

class SystemMessage(models.Model):
    toUser = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='toUser')
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    content = models.TextField(null=True)
    isRead = models.BooleanField(default=False)

