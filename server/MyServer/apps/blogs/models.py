from django.db import models

from apps.users.models import UserInfo
# Create your models here.


class Blog(models.Model):
    blog_id = models.CharField(primary_key=True,unique=True,max_length=100)
    title = models.CharField(max_length=50)
    authorId = models.CharField(max_length=50)
    authorName = models.CharField(max_length=50)
    link = models.URLField()
    descript =  models.CharField(max_length=100,null=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    userInfo = models.ForeignKey(UserInfo,on_delete=models.CASCADE, related_name='userInfo')
    to_blogId = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    name = models.CharField(max_length=50)
    def toJSON(self):
        import json
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

def getFileDict(filed):
    return dict([(attr, getattr(filed, attr)) for attr in [f.name for f in filed._meta.fields]])

class Reply(models.Model):
    #reply_id = models.CharField(primary_key=True,unique=True,max_length=100)
    reply_id = models.AutoField(primary_key=True)
    to_commentId = models.ForeignKey(Comment, related_name='reply_list',on_delete=models.CASCADE)
    to_blogId = models.CharField(max_length=50)
    to_username = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    userInfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    def toJSON(self):
        import json
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

class BlogMessage(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='BlogUser')
    toUser = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='BlogtoUser')
    msgType = models.CharField(max_length=20, choices=(('RE','reply'), ('CO','comment')))
    time = models.DateTimeField(auto_now=True)
    isRead = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

class testmedel(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=50)