import jwt
from django.contrib.auth import user_logged_in
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.tokens import RefreshToken

from social_media import settings
from . import models, serializers

class RegisterAPIView(generics.CreateAPIView):
    queryset = models.UserPost.objects.all()
    serializer_class = serializers.RegisterSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username',
                        'email', ]

class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']

            user = models.UserPost.objects.get(email=email, password=password)
            if user:
                try:
                    # payload = jwt_payload_handler(user)
                    token = jwt.encode(settings.SECRET_KEY)
                    user_details = {}
                    user_details['name'] = "%s %s" % (
                        user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)

                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.UserPost.objects.all()

class RegisterUserAPIView(generics.CreateAPIView):
    queryset = models.UserPost.objects.all()
    serializer_class = serializers.RegisterSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username',
                        'email',
                    ]
