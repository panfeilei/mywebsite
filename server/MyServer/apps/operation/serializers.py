from rest_framework import serializers

from .models import Favorite,Interest
class FavorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Favorite
        fields = '__all__'

class InterSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate(self, data):
        if data['user'] == data['toUserId']:
            raise serializers.ValidationError("不能关注自己")
        return data

    class Meta:
        model = Interest
        fields = '__all__'
