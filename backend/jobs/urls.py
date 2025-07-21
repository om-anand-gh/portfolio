from django.urls import path
from .views import GenerateEmbeddingView, SimilaritySearchView

urlpatterns = [
    path(
        "generate-embedding/",
        GenerateEmbeddingView.as_view(),
        name="generate-embedding",
    ),
    path(
        "similarity-search/", SimilaritySearchView.as_view(), name="similarity-search"
    ),
]
