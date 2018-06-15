from django.db import models
from django.db import models
from apps.blogs.models import MyUser
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='favo_list')
    blogId = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'blogId')

class Interest(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='inter_list')
    toUserId = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'toUserId')