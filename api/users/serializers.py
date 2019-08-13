from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'date_joined', 'first_name', 'last_name', 'is_active')


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_staff', 'first_name', 'last_name', 'is_active')

    def create(self, validated_data):
        passwd = validated_data.pop('password')
        u = User(**validated_data)
        u.set_password(passwd)
        u.is_active = True
        u.save()
        return u


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)

    def update(self, instance, validated_data):
        request = self.context['request']
        passwd = request.data.get('password')
        uname = request.data.get('username')
        lname = request.data.get('last_name')
        fname = request.data.get('first_name')
        active = request.data.get('is_active')
        c_u = User.objects.get(id=instance.id)
        if passwd:
            print('updatedp', passwd)
            c_u.set_password(passwd)
            c_u.save()
        if uname:
            print('updatedu', uname)
            c_u.username = uname
            c_u.save()
        if lname:
            c_u.last_name = lname
            c_u.save()
        if fname:
            c_u.first_name = fname
            c_u.save()
        if active:
            if active=='True':
                c_u.is_active=True
            else:
                c_u.is_active = True
        return c_u
