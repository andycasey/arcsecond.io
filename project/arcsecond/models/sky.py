from django.db import models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .coordinates import AstronomicalCoordinates
from .infos import *
from .constants import *

class Alias(models.Model):
    name = models.CharField(max_length=500)
    catalogue_url = models.URLField(null=True, blank=True)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="aliases", blank=True)
    exoplanet = models.ForeignKey('Exoplanet', null=True, related_name="aliases", blank=True)


class ObjectType(models.Model):
    value = models.CharField(max_length=500)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="object_types", blank=True)


class Exoplanet(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.OneToOneField(AstronomicalCoordinates, null=True, blank=True)
    parent_star = models.ForeignKey('AstronomicalObject', null=True, blank=True, related_name="planets")
    discovery_date = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)

    mass = models.OneToOneField(Mass, null=True, blank=True)
    radius = models.OneToOneField(Radius, null=True, blank=True)
    inclination = models.OneToOneField(Angle, null=True, blank=True, related_name="inclination")

    molecules_detected = models.CharField(max_length=100, null=True, blank=True)
    publication_status = models.CharField(max_length=200, null=True, blank=True)

    semi_major_axis = models.OneToOneField(EllipseAxis, null=True, blank=True, related_name="semi_major_axis")
    orbital_period = models.OneToOneField(Period, null=True, blank=True, related_name="orbital_period")
    eccentricity = models.OneToOneField(Eccentricity, null=True, blank=True)

    omega_angle = models.OneToOneField(Angle, null=True, blank=True, related_name="omega_angle")
    anomaly_angle = models.OneToOneField(Angle, null=True, blank=True, related_name="anomaly_angle")
    lambda_angle = models.OneToOneField(Angle, null=True, blank=True, related_name="lambda_angle")

    time_periastron = models.OneToOneField(JulianDay, null=True, blank=True, related_name="time_periastron")
    time_conjonction = models.OneToOneField(JulianDay, null=True, blank=True, related_name="time_conjonction")
    angular_distance = models.OneToOneField(Angle, null=True, blank=True, related_name="angular_distance")

    primary_transit = models.OneToOneField(JulianDay, null=True, blank=True, related_name="primary_transit")
    secondary_transit = models.OneToOneField(JulianDay, null=True, blank=True, related_name="secondary_transit")
    impact_parameter = models.OneToOneField(Angle, null=True, blank=True, related_name="impact_parameter")
    time_radial_velocity_zero = models.OneToOneField(JulianDay, null=True, blank=True, related_name="time_radial_velocity_zero")
    velocity_semiamplitude = models.OneToOneField(Velocity, null=True, blank=True)

    calculated_temperature = models.OneToOneField(Temperature, null=True, blank=True, related_name="calculated_temperature")
    measured_temperature = models.OneToOneField(Temperature, null=True, blank=True, related_name="measured_temperature")
    hottest_point_longitude = models.OneToOneField(Angle, null=True, blank=True, related_name="hottest_point_longitude")
    geometric_albedo = models.OneToOneField(Albedo, null=True, blank=True)
    surface_gravity = models.OneToOneField(Gravity, null=True, blank=True)

    DETECTION_METHOD_UNKNOWN = "unk"
    DETECTION_METHOD_RV = "rvs"
    DETECTION_METHOD_MICROLENSING = "mls"
    DETECTION_METHOD_TRANSIT = "tra"
    DETECTION_METHOD_TIMING = "tim"
    DETECTION_METHOD_ASTROMETRY = "ast"
    DETECTION_METHOD_IMAGING = "img"

    DETECTION_METHOD_KEYS = (
        DETECTION_METHOD_UNKNOWN,
        DETECTION_METHOD_RV,
        DETECTION_METHOD_MICROLENSING,
        DETECTION_METHOD_TRANSIT,
        DETECTION_METHOD_TIMING,
        DETECTION_METHOD_ASTROMETRY,
        DETECTION_METHOD_IMAGING,
    )

    DETECTION_METHOD_VALUES = (
        'Unknown',
        'Radial Velocity',
        'Microlensing',
        'Primary Transit',
        'Timing',
        'Astrometry',
        'Imaging'
    )

    DETECTION_METHOD_CHOICES = tuple(zip(DETECTION_METHOD_KEYS, DETECTION_METHOD_VALUES))

    detection_method = models.CharField(max_length=3, blank=True, choices=DETECTION_METHOD_CHOICES, default=DETECTION_METHOD_UNKNOWN)
    mass_detection_method = models.CharField(max_length=3, blank=True, choices=DETECTION_METHOD_CHOICES, default=DETECTION_METHOD_UNKNOWN)
    radius_detection_method = models.CharField(max_length=3, blank=True, choices=DETECTION_METHOD_CHOICES, default=DETECTION_METHOD_UNKNOWN)


class AstronomicalObjectManager(models.Manager):
    def get_with_aliases_or_create(self, name):
        try:
            obj = self.get(name=name)
        except ObjectDoesNotExist:

            try:
                alias = Alias.objects.get(name=name)
            except ObjectDoesNotExist:
                obj = AstronomicalObject(name=name)
                obj.save()
                return obj, True
            except MultipleObjectsReturned:
                aliases = self.filter(name=name)
                first = aliases.first()
                aliases.delete()
                first.save()
                return first.astronomical_object, False
            else:
                return alias.astronomical_object, False

        except MultipleObjectsReturned:
            objects = self.filter(name=name)
            first = objects.first()
            objects.delete()
            first.save()
            return first, False
        else:
            return obj, False


class AstronomicalObject(models.Model):
    objects = AstronomicalObjectManager()

    name = models.CharField(max_length=100)
    coordinates = models.OneToOneField(AstronomicalCoordinates, null=True, blank=True)

    mass = models.OneToOneField(Mass, null=True, blank=True)
    radius = models.OneToOneField(Radius, null=True, blank=True)
    distance = models.OneToOneField(Distance, null=True, blank=True)
    metallicity = models.OneToOneField(Metallicity, null=True, blank=True)
    age = models.OneToOneField(Age, null=True, blank=True)
    effective_temperature = models.OneToOneField(Temperature, null=True, blank=True)
    spectral_type = models.CharField(max_length=1000, null=True, blank=True)

    # Add Image Preview URLs