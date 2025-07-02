from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VisitCounter
from .serializers import VisitCounterSerializer


class VisitCounterView(APIView):
    def post(self, request):
        slug = "homepage"
        counter, _ = VisitCounter.objects.get_or_create(slug=slug)
        counter.count += 1
        counter.save()
        serializer = VisitCounterSerializer(counter)
        return Response(serializer.data, status=status.HTTP_200_OK)
