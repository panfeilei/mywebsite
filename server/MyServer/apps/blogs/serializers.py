from rest_framework import serializers

from .models import Comment,Blog,Reply


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'



class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    reply_list = ReplySerializer(many=True)
    class Meta:
        model = Comment
        fields = '__all__'