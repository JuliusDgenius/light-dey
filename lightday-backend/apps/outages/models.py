from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=255, unique=True)   # e.g., "Yaba"
    state = models.CharField(max_length=255, blank=True)   # e.g., "Lagos"
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.state}" if self.state else self.name


class OutageReport(models.Model):
    STATUS_CHOICES = [
        ("LIGHT", "Light Available"),
        ("NO_LIGHT", "No Light"),
    ]

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="outage_reports")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="outage_reports")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
