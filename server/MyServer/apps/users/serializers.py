from rest_framework import serializers

from .models import  UserMessage, SystemMessage
from apps.blogs.models import BlogMessage
from .models import UserInfo,MyUser


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    UserInfo = UserInfoSerializer()

    class Meta:
        model = MyUser
        fields = ('userId', 'username', 'UserInfo')


class UserMsgSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserMessage
        fields = '__all__'


class UserMsgSerializerGet(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False)
    user = MyUserSerializer()

    class Meta:
        model = UserMessage
        fields = '__all__'

class SysMsgSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = SystemMessage
        fields = '__all__'