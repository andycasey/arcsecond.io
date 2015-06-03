from rest_framework import serializers
from models import *

# Common

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person


class BibliographicReferenceSerializer(serializers.HyperlinkedModelSerializer):
    authors = PersonSerializer(many=True)

    class Meta:
        model = BibliographicReference

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ('warn', 'error', 'info', 'debug', 'http_status_code') if settings.DEBUG is True else ('warn', 'error', 'info', 'http_status_code')

# Sky

class AstronomicalCoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AstronomicalCoordinates
        fields = ("system", "right_ascension", "right_ascension_units", "declination", "declination_units", "epoch", "equinox")


class AliasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alias
        fields = ("name", "catalogue_url")


class ObjectTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ObjectType
        fields = ("value",)


class AstronomicalFluxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AstronomicalFlux
        fields = ("name", "value", "error_value", "bibcode")


class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = AstronomicalCoordinatesSerializer()
    aliases = AliasSerializer(many=True)
    object_types = ObjectTypeSerializer(many=True)
    fluxes = AstronomicalFluxSerializer(many=True)
    messages = MessagesSerializer()

    class Meta:
        model = AstronomicalObject
        fields = ("name", "coordinates", "aliases", "object_types", "fluxes", "messages")


# Earth

class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates
        fields = ("longitude", "latitude", "height", "east_positive")
        lookup_field = "url"


class ObservingSiteSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = CoordinatesSerializer()

    class Meta:
        model = ObservingSite
        fields = ("name", "coordinates", "IAUCode")
        lookup_field = "url"

