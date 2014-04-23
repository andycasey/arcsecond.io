
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
#  reference = BibliographicReferenceSerializer()
  class Meta:
    model = AstronomicalCoordinates
    fields = ("right_ascension", "declination", "epoch", "equinox", "source")

class AliasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Alias
    fields = ("value",)
  
class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
  coordinates = AstronomicalCoordinatesSerializer()
  aliases = serializers.HyperlinkedRelatedField(many=True, view_name='alias-list')
  #references = serializers.HyperlinkedRelatedField(many=True, view_name='reference-list')
  class Meta:
    model = AstronomicalObject
    fields = ("name", "coordinates", "aliases")

