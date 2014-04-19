
from rest_framework import serializers
from .models import *

class AstronomicalCoordinatesSerializer(serializers.ModelSerializer):
  class Meta:
    model = AstronomicalCoordinates
    fields = ("right_ascension", "declination", "epoch", "equinox")

class AstronomicalObjectSerializer(serializers.ModelSerializer):
  coordinates = AstronomicalCoordinatesSerializer()
  
  class Meta:
    model = AstronomicalObject
    fields = ("name", "coordinates",)

