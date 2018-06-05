from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50, unique=True, default="")
    userId = models.IntegerField(unique=True)
    iconUrl = models.URLField(default="/media/head.jpg")
    newlyTime = models.DateField(auto_now=True)

class MessageManager(models.Manager):
    def createMessage(self, m):
        msg = self.create(name=m.name, userId=m.userId,
                          time=m.time, content=m.content,
                          toUserId=m.toUserId, type=m.type,
                          fromBlog=m.fromBlog, link=m.link)
        return msg

class Message(models.Model):
    name = models.CharField(max_length=50, default="")
    userId = models.IntegerField()
    fromBlog = models.CharField(null=True, max_length=50)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    toUserId =  models.IntegerField()
    type = models.CharField(max_length=50)
    objects = MessageManager()
    link = models.URLField()

class UnreadMessage(models.Model):
    name = models.CharField(max_length=50, default="")
    userId = models.IntegerField()
    fromBlog = models.CharField(null=True, max_length=50)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    toUserId =  models.IntegerField()
    type = models.CharField(max_length=50)
    link = models.URLField()
