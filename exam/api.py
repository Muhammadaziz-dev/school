from .serializers import *
from .models import *
from rest_framework import generics
class GradeAPIView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializers