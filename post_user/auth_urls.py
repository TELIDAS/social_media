from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from . import views


urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify/', TokenVerifyView.as_view(), name='verify_token'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user-list/', views.UserListView.as_view(), name='user_list'),
    path('register/', views.RegisterUserAPIView.as_view(), name='register_user')
]