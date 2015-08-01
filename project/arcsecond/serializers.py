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
        fields = ("value", "error_max", "error_min", "bibcode")

class AlbedoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albedo
        fields = ("value", "error_max", "error_min", "bibcode")

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

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Mass.MASSES_VALUES[Mass.MASSES_KEYS.index(obj.unit)]

class RadiusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radius
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Radius.RADIUS_VALUES[Radius.RADIUS_KEYS.index(obj.unit)]

class AgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Age
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Age.AGE_VALUES[Age.AGE_KEYS.index(obj.unit)]


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Temperature.TEMP_VALUES[Temperature.TEMP_KEYS.index(obj.unit)]


class MetallicitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metallicity
        fields = ("value", "unit", "error", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Metallicity.METAL_VALUES[Metallicity.METAL_KEYS.index(obj.unit)]


class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Distance.DISTANCE_VALUES[Distance.DISTANCE_KEYS.index(obj.unit)]


class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Period.PERIOD_VALUES[Period.PERIOD_KEYS.index(obj.unit)]


class EllipseAxisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EllipseAxis
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return EllipseAxis.AXIS_VALUES[EllipseAxis.AXIS_KEYS.index(obj.unit)]

class AngleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Angle
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Angle.ANGLE_VALUES[Angle.ANGLE_KEYS.index(obj.unit)]

class VelocitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class GravitySerializer(serializers.HyperlinkedModelSerializer):
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

    coordinates = AstronomicalCoordinatesSerializer(required=False)
    parent_star = AstronomicalObjectSerializer()

    mass = MassSerializer(required=False)
    radius = RadiusSerializer(required=False)
    inclination = AngleSerializer(required=False)

    semi_major_axis = EllipseAxisSerializer(required=False)
    orbital_period = PeriodSerializer(required=False)
    eccentricity = EccentricitySerializer(required=False)
    omega = AngleSerializer(required=False)
    time_periastron = JulianDaySerializer(required=False)
    angular_distance = AngleSerializer(required=False)

    primary_transit = JulianDaySerializer(required=False)
    secondary_transit = JulianDaySerializer(required=False)
    anomaly_angle = AngleSerializer(required=False)
    impact_parameter_b = AngleSerializer(required=False)
    time_vr0 = JulianDaySerializer(required=False)
    velocity_semiamplitude_K = VelocitySerializer(required=False)

    calculated_temperature = TemperatureSerializer(required=False)
    measured_temperature = TemperatureSerializer(required=False)
    hottest_point_longitude = AngleSerializer(required=False)
    geometric_albedo = AlbedoSerializer(required=False)
    surface_gravity = GravitySerializer(required=False)

    detection_method = serializers.SerializerMethodField()
    mass_detection_method = serializers.SerializerMethodField()
    radius_detection_method = serializers.SerializerMethodField()

    def get_detection_method(self, obj):
        return Exoplanet.DETECTION_METHOD_VALUES[Exoplanet.DETECTION_METHOD_KEYS.index(obj.detection_method)]

    def get_mass_detection_method(self, obj):
        return Exoplanet.DETECTION_METHOD_VALUES[Exoplanet.DETECTION_METHOD_KEYS.index(obj.detection_method)]

    def get_radius_detection_method(self, obj):
        return Exoplanet.DETECTION_METHOD_VALUES[Exoplanet.DETECTION_METHOD_KEYS.index(obj.detection_method)]

######################## Archives ########################

class ESOProgrammeSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ESOProgrammeSummary
        lookup_field = "programme_id"

class HSTProgrammeSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HSTProgrammeSummary
        lookup_field = "programme_id"
