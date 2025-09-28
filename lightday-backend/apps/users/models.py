from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model inheriting from AbstractUser.
    Email is the unique identifier for authentication instead of username.
    """
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    # Set the email field as the username field for authentication
    USERNAME_FIELD = "email"
    # The default 'username' is still required for user creation, 
    # along with any other fields in this list.
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
