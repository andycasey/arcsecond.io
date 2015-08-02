
from django.core import exceptions

from rest_framework import views
from rest_framework import response
from rest_framework import status

from project.arcsecond import connectors
from project.arcsecond import serializers
from project.arcsecond import models
from project.arcsecond import mixins

class CoordinatesConverterDetailAPIView(mixins.RequestLogViewMixin, views.APIView):

    def get(self, request, ra, dec, format=None):
        coordinates = models.AstronomicalCoordinates(right_ascension=float(ra), declination=float(dec))
        coordinates.save()
        conversion = models.CoordinatesConversion()
        conversion.input_coordinates = coordinates
        conversion.save()
        serializer = serializers.CoordinatesConversionSerializer(conversion)
        return response.Response(serializer.data)


