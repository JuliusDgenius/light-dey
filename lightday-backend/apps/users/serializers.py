from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Handles validation and creation of a new user, including password hashing.
    """
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "location")
        extra_kwargs = {
            "password": {"write_only": True}, # Ensure password is not sent back
        }

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        This method overrides the default to handle password hashing.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            location=validated_data.get("location")
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for representing a user's profile.

    Excludes sensitive information like the password.
    """
    class Meta:
        model = User
        fields = ("id", "username", "email", "location", "date_joined")
