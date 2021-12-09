from rest_framework.viewsets import ModelViewSet
from . import serializers, models

class PostView(ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

