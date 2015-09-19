from rest_framework import serializers
from project.arcsecond.models.infos import *

######################## Infos ########################


class JulianDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = JulianDay
        fields = ("value", "error_max", "error_min", "bibcode")

class AlbedoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albedo
        fields = ("value", "error_max", "error_min", "bibcode")

class EccentricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Eccentricity
        fields = ("value", "error_max", "error_min", "bibcode")

class FluxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flux
        fields = ("name", "value", "error_max", "error_min", "bibcode")

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("first_magnitude_name", "second_magnitude_name", "value", "error", "bibcode")

class MassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mass
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Mass.MASSES_VALUES[Mass.MASSES_KEYS.index(obj.unit)]

class RadiusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radius
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Radius.RADIUS_VALUES[Radius.RADIUS_KEYS.index(obj.unit)]

class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Age.AGE_VALUES[Age.AGE_KEYS.index(obj.unit)]


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Temperature.TEMP_VALUES[Temperature.TEMP_KEYS.index(obj.unit)]


class MetallicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Metallicity
        fields = ("value", "unit", "error", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Metallicity.METAL_VALUES[Metallicity.METAL_KEYS.index(obj.unit)]


class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Distance.DISTANCE_VALUES[Distance.DISTANCE_KEYS.index(obj.unit)]


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Period.PERIOD_VALUES[Period.PERIOD_KEYS.index(obj.unit)]


class EllipseAxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = EllipseAxis
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return EllipseAxis.AXIS_VALUES[EllipseAxis.AXIS_KEYS.index(obj.unit)]

class AngleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angle
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Angle.ANGLE_VALUES[Angle.ANGLE_KEYS.index(obj.unit)]

class VelocitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class GravitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")


