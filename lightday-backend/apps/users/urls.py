from django.urls import path
from .views import RegisterView, EmailTokenObtainPairView, MeView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register", RegisterView.as_view(), name="auth-register"),
    path("login", EmailTokenObtainPairView.as_view(), name="auth-login"),
    path("refresh", TokenRefreshView.as_view(), name="auth-refresh"),
    path("me", MeView.as_view(), name="auth-me"),
]
