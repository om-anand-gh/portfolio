from pgvector.django import (
    MaxInnerProduct,
    CosineDistance,
    L1Distance,
)
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.llm import generate_embeddings
from utils.text import extract_lines

from .models import Job, JobEmbedding, Country, Province
from .serializers import GenerateEmbeddingSerializer, SimilaritySearchSerializer, LocationCountrySerializer, LocationProvinceSerializer

class GenerateEmbeddingView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GenerateEmbeddingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_id = serializer.validated_data["job_id"]
        job = Job.objects.get(id=job_id)

        fields_to_embed = [
            "qualifications",
            "responsibilities",
            "preferred_qualifications",
        ]

        total_chunks = 0

        for field in fields_to_embed:
            content = getattr(job, field)
            lines = extract_lines(content)

            embeddings = generate_embeddings(lines)

            embeddings_to_create = [
                JobEmbedding(
                    job=job,
                    field=field,
                    line_number=i,
                    content=line,
                    embedding=embedding,
                )
                for i, (line, embedding) in enumerate(zip(lines, embeddings))
            ]

            JobEmbedding.objects.bulk_create(
                embeddings_to_create, ignore_conflicts=True
            )
            total_chunks += len(embeddings_to_create)

        return Response(
            {"detail": f"Generated {total_chunks} embeddings for Job '{job.title}'."}
        )


class SimilaritySearchView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SimilaritySearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data["question"]
        top_n = serializer.validated_data["top_n"]

        query_embedding = generate_embeddings(question)[0]

        queryset = JobEmbedding.objects.annotate(
            cosine_similarity=1 - CosineDistance("embedding", query_embedding),
            max_inner_product=MaxInnerProduct("embedding", query_embedding),
            l1_distance=L1Distance("embedding", query_embedding),
        ).all()

        results = queryset.values(
            "id",
            "content",
            "field",
            "line_number",
            "cosine_similarity",
            "max_inner_product",
            "l1_distance",
        )

        # Sort and rank according to each metric
        def rank_results(results, key, reverse=True):
            sorted_items = sorted(results, key=lambda x: x[key], reverse=reverse)
            ranks = {}
            for idx, item in enumerate(sorted_items, start=1):
                ranks[item["id"]] = idx
            return ranks

        cosine_ranks = rank_results(results, "cosine_similarity", reverse=True)
        maxip_ranks = rank_results(results, "max_inner_product", reverse=True)
        l1_ranks = rank_results(
            results, "l1_distance", reverse=False
        )  # L1 distance: lower is better

        # Add rank info to each result
        for r in results:
            r["rank_cosine_similarity"] = cosine_ranks.get(r["id"], None)
            r["rank_max_inner_product"] = maxip_ranks.get(r["id"], None)
            r["rank_l1_distance"] = l1_ranks.get(r["id"], None)

        # Now, slice top_n by cosine_similarity (or whichever you want)
        results_sorted = sorted(
            results, key=lambda x: x["cosine_similarity"], reverse=True
        )[:top_n]

        return Response({"results": results_sorted})

class LocationCountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = LocationCountrySerializer


class LocationProvinceList(generics.ListAPIView):
    serializer_class = LocationProvinceSerializer
    queryset = Province.objects.all()

    def get_queryset(self):
        country_code = self.request.query_params.get("country_code")
        if country_code:
            try:
                country = Country.objects.get(code__iexact=country_code)
                return Province.objects.filter(country=country)
            except Country.DoesNotExist:
                return Province.objects.none()
        return super().get_queryset()

    def perform_create(self, serializer):
        country_code = self.request.data.get("country_code")
        if not country_code:
            raise ValidationError({"country_code": "This field is required."})
        try:
            country = Country.objects.get(code__iexact=country_code)
        except Country.DoesNotExist:
            raise ValidationError({"country_code": f"Country with code '{country_code}' does not exist."})
        serializer.save(country=country)
