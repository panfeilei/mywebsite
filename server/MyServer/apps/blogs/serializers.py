from rest_framework import serializers

from .models import Comment,Blog,Reply,testmedel
from apps.users.serializers import UserInfoSerializer
from apps.blogs.models import BlogMessage

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

class BlogSerializer(serializers.ModelSerializer):
    authorId = UserInfoSerializer()
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    comment_list = CommentSerializer(many=True)
    class Meta:
        model = Blog
        fields = '__all__'

class BlogMsgSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    blog = BlogSerializer()
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = BlogMessage
        fields = '__all__'

class testModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = testmedel
        fields = '__all__'