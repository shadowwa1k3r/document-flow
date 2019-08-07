from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id',)


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        passwd = validated_data.pop('password')
        u = User(**validated_data)
        u.set_password(passwd)
        u.save()
        return u
