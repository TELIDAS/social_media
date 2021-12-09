from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'', views.PostView, basename='post_view')


urlpatterns = [
    path('post/', include(router.urls)),
]
