from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class NotificationsListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response([])


urlpatterns = [
    path("", NotificationsListView.as_view(), name="notifications-list"),
]
