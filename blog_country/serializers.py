from rest_framework import serializers
from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ['id',
                  'name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostImage
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    comment = CommentSerializer()

    class Meta:
        model = models.Post
        fields = '__all__'
