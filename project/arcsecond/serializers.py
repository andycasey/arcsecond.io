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

# class MessagesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Messages
#         fields = ('warn', 'error', 'info', 'debug', 'http_status_code') if settings.DEBUG is True else ('warn', 'error', 'info', 'http_status_code')

######################## Infos ########################


class JulianDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JulianDay
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class AlbedoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albedo
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class EccentricitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eccentricity
        fields = ("value", "error_max", "error_min", "bibcode")

class FluxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flux
        fields = ("name", "value", "error_max", "error_min", "bibcode")

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ("first_magnitude_name", "second_magnitude_name", "value", "error", "bibcode")

class MassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mass
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class RadiusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radius
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class AgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Age
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class MetallicitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metallicity
        fields = ("value", "unit", "error", "error_max", "error_min", "bibcode")

class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class EllipseAxisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EllipseAxis
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class AngularDistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AngularDistance
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class AngleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Angle
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class VelocitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class GravitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class ParallaxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")



######################## Earth ########################

class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates


class ObservingSiteSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = CoordinatesSerializer()

    class Meta:
        model = ObservingSite
        lookup_field = "name"



######################## Objects Properties ########################

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


######################## Objects ########################

class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AstronomicalObject
        lookup_field = "name"

    coordinates = AstronomicalCoordinatesSerializer()
    aliases = AliasSerializer(many=True, required=False)
    object_types = ObjectTypeSerializer(many=True, required=False)
    fluxes = FluxSerializer(many=True, required=False)

    mass = MassSerializer(required=False)


class ExoplanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exoplanet

    mass = MassSerializer(required=False)
    radius = RadiusSerializer(required=False)
    orbital_period = PeriodSerializer(required=False)
    semi_major_axis = EllipseAxisSerializer(required=False)
    eccentricity = EccentricitySerializer(required=False)
    inclination = AngleSerializer(required=False)
    omega = AngleSerializer(required=False)
    geometric_albedo = AlbedoSerializer(required=False)




######################## Archives ########################

class ESOProgrammeSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ESOProgrammeSummary
        lookup_field = "programme_id"
