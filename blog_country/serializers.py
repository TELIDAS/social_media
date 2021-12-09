from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostImage
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ['id',
                  'title',
                  'description',
                  'image',
                  'user',
                  'country',
                  'comment_model',]


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = ['id',
                  'name',
                  'country_post',]
