from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from post_user.permissions import IsClient
from . import serializers, models
from rest_framework import generics

class PostView(ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    # permission_classes = [IsClient, AllowAny]


class CountryView(generics.ListCreateAPIView):
    serializer_class = serializers.CountrySerializer
    queryset = models.Country.objects.all()

class CommentView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()