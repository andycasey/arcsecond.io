
from rest_framework import generics
from rest_framework import permissions

from .models import AstronomicalObject
from .serializers import AstronomicalObjectSerializer

class AstronomicalObjectDetail(generics.RetrieveAPIView):
  model = AstronomicalObject
  serializer_class = AstronomicalObjectSerializer

