from django.conf import settings
from django.db import models


class Notification(models.Model):
    # Notification model
    NOTIF_TYPE_CHOICES = [
        ("PUSH", "Push"),
        ("EMAIL", "Email"),
        ("SMS", "SMS"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    notif_type = models.CharField(max_length=10, choices=NOTIF_TYPE_CHOICES)
    status = models.CharField(max_length=10, default="PENDING")  # SENT / FAILED / PENDING
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.notif_type}"
