from rest_framework import serializers
from .models import *

# Common

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person


class BibliographicReferenceSerializer(serializers.HyperlinkedModelSerializer):
    authors = PersonSerializer(many=True)

    class Meta:
        model = BibliographicReference


# Sky

class AstronomicalCoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AstronomicalCoordinates
        fields = ("right_ascension", "declination", "epoch", "equinox", "source")


class AliasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alias
        fields = ("name", "catalogue_url")


class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = AstronomicalCoordinatesSerializer()
    aliases = AliasSerializer(many=True)

    class Meta:
        model = AstronomicalObject
        fields = ("name", "coordinates", "aliases")


# Earth

class TerrestrialCoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TerrestrialCoordinates
        fields = ("longitude", "latitude", "altitude", "east_positive")
        lookup_field = "url"


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = TerrestrialCoordinatesSerializer()

    class Meta:
        model = Site
        fields = ("name", "coordinates")
        lookup_field = "url"


class ObservingSiteSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = TerrestrialCoordinatesSerializer()

    class Meta:
        model = ObservingSite
        fields = ("name", "coordinates", "IAUCode")
        lookup_field = "url"

