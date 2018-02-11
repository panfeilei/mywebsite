from django.db import models

# Create your models here.
class MyUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()