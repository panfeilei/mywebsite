from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    userId = models.IntegerField(unique=True)
    iconUrl = models.URLField(default="/media/head.jpg")
    newlyTime = models.DateField(auto_now=True)
