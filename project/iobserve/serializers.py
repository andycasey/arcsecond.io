
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


class AliasSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Alias
    fields = ("name",)


class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
  coordinates = AstronomicalCoordinatesSerializer()
  aliases = AliasSerializer(many=True)

  class Meta:
    model = AstronomicalObject
    fields = ("name", "coordinates", "aliases")
