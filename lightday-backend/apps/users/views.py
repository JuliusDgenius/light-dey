from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from .serializers import UserRegisterSerializer, UserProfileSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    """
    Custom view for obtaining a token pair (access and refresh) using email.
    """
    # Since the User model's USERNAME_FIELD is 'email', 
    # the default TokenObtainPairSerializer will work correctly
    # by expecting 'email' and 'password' fields in the request.
    pass

class UserRegisterView(generics.CreateAPIView):
    """
    View for registering a new user. Publicly accessible.
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveAPIView):
    """
    View to retrieve the profile of the currently authenticated user.
    Requires authentication.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Returns the authenticated user associated with the request.
        """
        return self.request.user
