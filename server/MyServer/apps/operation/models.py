from django.db import models
from django.db import models
from apps.users.models import MyUser, UserInfo
from apps.blogs.models import Blog
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='favo_list', db_column='user')
    blogId = models.CharField(max_length=100)
    class Meta:
        unique_together = ('user', 'blogId')

class Interest(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='inter_list', db_column='user')
    toUserId = models.ForeignKey(MyUser, on_delete=models.CASCADE, db_column='toUserId')
    class Meta:
        unique_together = ('user', 'toUserId')

