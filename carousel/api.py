from rest_framework import generics
from rest_framework.response import Response

from carousel.models import Carousel
from .serializers import CarouselSerializer

class CarouselListAPIView(generics.ListAPIView):
    serializer_class = CarouselSerializer

    def get_queryset(self):
        # Oxirgi 4 ta carouselni olish
        latest_carousels = Carousel.objects.all().order_by('-id')[:10]
        return latest_carousels

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
