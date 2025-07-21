from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GenerateEmbeddingView, SimilaritySearchView, LocationCountryList, LocationProvinceList


urlpatterns = [
    path(
        "generate-embedding/",
        GenerateEmbeddingView.as_view(),
        name="generate-embedding",
    ),
    path(
        "similarity-search/", SimilaritySearchView.as_view(), name="similarity-search"
    ),
    path("location/country/", LocationCountryList.as_view()),
    path("location/province/", LocationProvinceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
