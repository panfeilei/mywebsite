from django.db import models

from apps.users.models import UserInfo, MyUser
# Create your models here.

class Category(models.Model):
    categoryId = models.CharField(primary_key=True,unique=True,max_length=100)
    name = models.CharField(max_length=50, null=False, blank=False)
    value = models.CharField(max_length=100)

class Blog(models.Model):
    blogId = models.CharField(primary_key=True,unique=True,max_length=100)
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs',  db_column='category')
    authorId = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='userbloglist', db_column='authorId')
    link = models.URLField()
    descript = models.CharField(max_length=100,null=True)
    content = models.TextField()
    readNum = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    userInfo = models.ForeignKey(UserInfo,on_delete=models.CASCADE, related_name='userInfo', db_column='userInfo')
    to_blogId = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name='comment_list')
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
    replyId = models.AutoField(primary_key=True)
    to_commentId = models.ForeignKey(Comment, related_name='reply_list',on_delete=models.CASCADE,db_column='to_commentId')
    to_blogId = models.CharField(max_length=50)
    to_username = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    userInfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='userInfo')
    def toJSON(self):
        import json
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

class BlogMessage(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='BlogUser', db_column='user')
    toUser = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='BlogtoUser', db_column='toUser')
    msgType = models.CharField(max_length=20, choices=(('RE','reply'), ('CO','comment')))
    time = models.DateTimeField(auto_now=True)
    isRead = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE, db_column='blog')

class testmedel(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
