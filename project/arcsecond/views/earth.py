
from rest_framework import generics

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class CoordinatesDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.ObservingSite.objects.all().values_list('coordinates', flat=True)
    serializer_class = serializers.CoordinatesSerializer

