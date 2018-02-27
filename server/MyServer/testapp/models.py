from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,BaseUserManager,AbstractUser
from django import forms
from django.utils.http import urlquote
from django.core.serializers.json import DjangoJSONEncoder
# Create your models here.
class MyUser(AbstractUser):
    #username = models.CharField(max_length=50, unique=True, default="")
    userid = models.IntegerField(unique=True, default=0)
    #userid = models.AutoField(primary_key=True)
    headlink = models.CharField(max_length=50, default="/")
    #USERNAME_FIELD = 'username'

class Blog(models.Model):
    blog_id = models.CharField(primary_key=True,unique=True,max_length=100)
    title = models.CharField(max_length=50)
    link = models.URLField()
    descript =  models.CharField(max_length=100,null=True)
    content = models.TextField()
    
class Comment(models.Model):
    #comment_id = models.CharField(primary_key=True,unique=True,max_length=100)
    comment_id = models.AutoField(primary_key=True)
    to_blogId = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    userid = models.IntegerField()
    def toJSON(self):
        import json
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
    # username = models.CharField(max_length=20)
    # headlink = models.CharField(max_length=100)
    
class Reply(models.Model):
    #reply_id = models.CharField(primary_key=True,unique=True,max_length=100)
    reply_id = models.AutoField(primary_key=True)
    to_commentId = models.IntegerField()
    to_blogId = models.CharField(max_length=50)
    to_username = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    userid = models.IntegerField()
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]), cls=DjangoJSONEncoder)
    # username = models.CharField(max_length=20)
    # headlink = models.CharField(max_length=50)



class testmedel(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()