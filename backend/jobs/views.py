from django.conf import settings
from openai import AzureOpenAI
from pgvector.django import CosineDistance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Job, JobEmbedding
from .serializers import GenerateEmbeddingSerializer, SimilaritySearchSerializer


client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version="2024-10-21",
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
)


class GenerateEmbeddingView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GenerateEmbeddingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_id = serializer.validated_data["job_id"]

        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response(
                {"detail": "Job not found."}, status=status.HTTP_404_NOT_FOUND
            )

        embedding_model = settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT
        fields_to_embed = [
            "qualifications",
            "responsibilities",
            "preferred_qualifications",
        ]

        total_chunks = 0

        for field in fields_to_embed:
            content = getattr(job, field)
            if not content:
                continue

            lines = [line.strip() for line in content.splitlines() if line.strip()]
            if not lines:
                continue

            try:
                response = client.embeddings.create(
                    input=lines,
                    model=embedding_model,
                )
            except Exception as e:
                return Response(
                    {"error": f"Embedding failed for field '{field}': {str(e)}"},
                    status=500,
                )

            for i, (line, result) in enumerate(zip(lines, response.data)):
                JobEmbedding.objects.update_or_create(
                    job=job,
                    field=field,
                    line_number=i,
                    defaults={"content": line, "embedding": result.embedding},
                )
                total_chunks += 1

        return Response(
            {"detail": f"Generated {total_chunks} embeddings for Job '{job.title}'."},
            status=status.HTTP_200_OK,
        )


class SimilaritySearchView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SimilaritySearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data["question"]
        top_n = serializer.validated_data["top_n"]
        model = settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT

        try:
            response = client.embeddings.create(
                input=question,
                model=model,
            )
        except Exception as e:
            return Response(
                {"error": f"Embedding generation failed: {str(e)}"}, status=500
            )

        query_embedding = response.data[0].embedding

        try:
            results = (
                JobEmbedding.objects.annotate(
                    similarity=1 - CosineDistance("embedding", query_embedding)
                )
                .order_by("-similarity")[:top_n]
                .values("content", "field", "line_number", "similarity")
            )
        except Exception as e:
            return Response(
                {"error": f"Similarity search failed: {str(e)}"}, status=500
            )

        return Response({"results": results}, status=status.HTTP_200_OK)
