from rest_framework import serializers
from .models import VisitCounter


class VisitCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitCounter
        fields = ["slug", "count"]
