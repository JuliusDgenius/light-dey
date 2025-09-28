from django.urls import include, path

urlpatterns = [
    path("auth/", include("apps.users.urls")),
    path("areas/", include("apps.outages.urls")),
    path("outages/", include("apps.outages.urls")),
    path("notifications/", include("apps.notifications.urls")),
]
