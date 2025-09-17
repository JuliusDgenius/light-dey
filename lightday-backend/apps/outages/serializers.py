from rest_framework import serializers
from .models import Area, OutageReport


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "name", "state", "latitude", "longitude"]


class OutageReportSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    area = AreaSerializer(read_only=True)
    area_id = serializers.PrimaryKeyRelatedField(
        queryset=Area.objects.all(), source="area", write_only=True
    )

    class Meta:
        model = OutageReport
        fields = [
            "id",
            "user",
            "area",
            "area_id",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "user", "area", "created_at"]
