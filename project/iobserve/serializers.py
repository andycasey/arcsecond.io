
from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Person


class BibliographicReferenceSerializer(serializers.HyperlinkedModelSerializer):
  authors = serializers.HyperlinkedRelatedField(many=True, view_name='authors-list')
  class Meta:
    model = BibliographicReference


class AstronomicalCoordinatesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = AstronomicalCoordinates
    fields = ("right_ascension", "declination", "epoch", "equinox", "source")
  

class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
  coordinates = AstronomicalCoordinatesSerializer()
  aliases = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='alias-list')

  class Meta:
    model = AstronomicalObject
    fields = ("name", "coordinates", "aliases")


class AliasSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Alias
    fields = ("name",)
