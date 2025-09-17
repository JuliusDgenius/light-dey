from django.urls import path
from .views import (
    AreaListCreateView,
    ReportOutageView,
    AreaReportsView,
    NearbyReportsView,
    LatestReportsView,
)

urlpatterns = [
    path("", AreaListCreateView.as_view(), name="areas-list-create"),
]

# Outages
urlpatterns += [
    path("report", ReportOutageView.as_view(), name="outages-report"),
    path("area/<str:name>", AreaReportsView.as_view(), name="outages-area"),
    path("nearby", NearbyReportsView.as_view(), name="outages-nearby"),
    path("latest", LatestReportsView.as_view(), name="outages-latest"),
]
