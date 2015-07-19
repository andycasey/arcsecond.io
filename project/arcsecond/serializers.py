from django.conf import settings
from rest_framework import serializers
from .models import *

######################## Common ########################

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

######################## Infos ########################

class JulianDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JulianDay
        fields = ("value", "error", "bibcode")

class AlbedoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albedo
        fields = ("value", "error", "bibcode")

class EccentricitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eccentricity
        fields = ("value", "error", "bibcode")

class FluxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flux
        fields = ("name", "value", "error", "bibcode")

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ("first_magnitude_name", "second_magnitude_name", "value", "error", "bibcode")

class MassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mass
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class RadiusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radius
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class AgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Age
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class MetallicitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metallicity
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class EllipseAxisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EllipseAxis
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class AngularDistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AngularDistance
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class AngleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Angle
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class VelocitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class GravitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

class ParallaxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error", "error_up", "error_down", "bibcode")

######################## Earth ########################

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



######################## Sky ########################

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


class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AstronomicalObject
        fields = ("name", "coordinates", "aliases", "object_types", "fluxes", "messages")

    coordinates = AstronomicalCoordinatesSerializer()
    aliases = AliasSerializer(many=True)
    object_types = ObjectTypeSerializer(many=True)
    fluxes = FluxSerializer(many=True)
    messages = MessagesSerializer()


class ExoplanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exoplanet
        fields = ("name", "messages")

    messages = MessagesSerializer()
