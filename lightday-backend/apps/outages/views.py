from math import radians, sin, cos, asin, sqrt
 
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Area, OutageReport
from .serializers import AreaSerializer, OutageReportSerializer

 
class AreaListCreateView(generics.ListCreateAPIView):
    queryset = Area.objects.all().order_by("name")
    serializer_class = AreaSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class ReportOutageView(generics.CreateAPIView):
    serializer_class = OutageReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AreaReportsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, name: str):
        try:
            area = Area.objects.get(name__iexact=name)
        except Area.DoesNotExist:
            return Response({"detail": "Area not found"}, status=404)
        reports = OutageReport.objects.filter(area=area).order_by("-created_at")[:100]
        return Response({
            "area": AreaSerializer(area).data,
            "reports": OutageReportSerializer(reports, many=True).data,
        })


class LatestReportsView(generics.ListAPIView):
    serializer_class = OutageReportSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return OutageReport.objects.select_related("area", "user").order_by("-created_at")[:100]


def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r_km = 6371
    return c * r_km


class NearbyReportsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            lat = float(request.query_params.get("lat"))
            lng = float(request.query_params.get("lng"))
            radius = float(request.query_params.get("radius", 5))
        except (TypeError, ValueError):
            return Response({"detail": "Invalid or missing coordinates"}, status=400)

        areas = Area.objects.exclude(latitude=None).exclude(longitude=None)
        nearby_area_ids = []
        for area in areas:
            d = haversine(float(area.latitude), float(area.longitude), lat, lng)
            if d <= radius:
                nearby_area_ids.append(area.id)

        reports = OutageReport.objects.filter(area_id__in=nearby_area_ids).order_by("-created_at")[:200]
        return Response({
            "user_location": {"latitude": lat, "longitude": lng},
            "nearby_reports": OutageReportSerializer(reports, many=True).data,
        })
