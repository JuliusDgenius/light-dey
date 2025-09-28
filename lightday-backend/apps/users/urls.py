from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    EmailTokenObtainPairView,
    UserRegisterView,
    UserProfileView,
)

urlpatterns = [
    path("register", UserRegisterView.as_view(), name="auth-register"),
    path("login", EmailTokenObtainPairView.as_view(), name="auth-login"),
    path("me", UserProfileView.as_view(), name="auth-me"),
    path("refresh", TokenRefreshView.as_view(), name="auth-refresh"),
]
