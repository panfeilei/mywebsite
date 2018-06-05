from django.db import models
from django.db import models
from blogs.models import User
# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogId = models.CharField(max_length=100)

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    toUserId = models.ForeignKey(User, on_delete=models.CASCADE)