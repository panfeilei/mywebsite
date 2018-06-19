from rest_framework import serializers

from .models import  UserMessage, SystemMessage
from apps.blogs.models import BlogMessage
from .models import UserInfo
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class UserMsgSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    user = UserInfoSerializer()
    class Meta:
        model = UserMessage
        fields = '__all__'


class SysMsgSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = SystemMessage
        fields = '__all__'