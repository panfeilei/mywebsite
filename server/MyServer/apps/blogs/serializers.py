from rest_framework import serializers

from .models import Comment,Blog,Reply,testmedel,MyUser
from apps.users.models import UserInfo
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    userInfo = UserInfoSerializer()
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = Reply
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    userInfo = UserInfoSerializer()
    reply_list = ReplySerializer(many=True)
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = Comment
        fields = '__all__'


class testModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = testmedel
        fields = '__all__'