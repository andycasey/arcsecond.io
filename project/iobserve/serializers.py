
from rest_framework import serializers
from .models import AstronomicalObject


class AstronomicalObjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = AstronomicalObject

