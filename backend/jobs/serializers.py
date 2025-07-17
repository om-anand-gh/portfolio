from rest_framework import serializers

class GenerateEmbeddingSerializer(serializers.Serializer):
    job_id = serializers.UUIDField()

class SimilaritySearchSerializer(serializers.Serializer):
    question = serializers.CharField()
    top_n = serializers.IntegerField(required=False, default=10, min_value=1, max_value=100)

