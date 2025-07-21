from rest_framework import serializers
from .models import Job, Country, Province

class GenerateEmbeddingSerializer(serializers.Serializer):
    job_id = serializers.UUIDField()

    def validate_job_id(self, value):
        if not Job.objects.filter(id=value).exists():
            raise serializers.ValidationError("Job with this ID does not exist.")
        return value


class SimilaritySearchSerializer(serializers.Serializer):
    question = serializers.CharField()
    top_n = serializers.IntegerField(
        required=False, default=10, min_value=1, max_value=100
    )

class LocationCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code']

class LocationProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'code']

