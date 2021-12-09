from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserPost
        fields = ['id',
                  'username',
                  'email',
                  'first_name',
                  'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=models.UserPost.objects.all())]
    ),
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=models.UserPost.objects.all())]
    )

    class Meta:
        model = models.UserPost
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  )
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserPost
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  )
        extra_kwargs = {
            'password': {'write_only': True},
        }