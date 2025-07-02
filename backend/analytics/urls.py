from django.urls import path
from .views import VisitCounterView

urlpatterns = [
    path("track-visit/", VisitCounterView.as_view(), name="track-visit"),
]
