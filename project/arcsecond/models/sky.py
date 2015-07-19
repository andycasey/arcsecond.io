
from .infos import *
from .constants import *
from django.db import models

class AstronomicalCoordinates(models.Model):

    SYSTEM_ICRS = "ICRS"
    SYSTEM_FK5 = "FK5"
    SYSTEM_FK4 = "FK4"
    SYSTEM_FK4NOTERMS = "FK4NoETerms"
    SYSTEM_GALACTIC = "Galactic"
    SYSTEM_ALTAZ = "AltAz"

    SYSTEMS_CHOICES = (
        (SYSTEM_ICRS, 'ICRS'),
        (SYSTEM_FK5, 'FK5'),
        (SYSTEM_FK4, 'FK4'),
        (SYSTEM_FK4NOTERMS, 'FK4NoETerms'),
        (SYSTEM_GALACTIC, 'Galactic'),
        (SYSTEM_ALTAZ, 'AltAz'),
    )

    system = models.CharField(max_length=20, choices=SYSTEMS_CHOICES, default=SYSTEM_ICRS)

    right_ascension = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    right_ascension_units = models.CharField(max_length=100, default='degrees')

    declination = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    declination_units = models.CharField(max_length=100, default='degrees')

    epoch = models.FloatField(default=J2000)
    equinox = models.FloatField(default=J2000)

    def are_empty(self):
        return self.right_ascension == NOT_A_SCIENTIFIC_NUMBER or \
               self.declination == NOT_A_SCIENTIFIC_NUMBER or \
               self.epoch == NOT_A_SCIENTIFIC_NUMBER

    def __unicode__(self):
        return u"(R.A.: %.8f, Dec: %.8f, epoch: %.2f, equinox: %.2f)"%(self.right_ascension, self.declination, self.epoch, self.equinox)


class Alias(models.Model):
    name = models.CharField(max_length=500)
    catalogue_url = models.URLField(null=True)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="aliases", blank=True)
    exoplanet = models.ForeignKey('Exoplanet', null=True, related_name="aliases", blank=True)


class ObjectType(models.Model):
    value = models.CharField(max_length=500)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="object_types", blank=True)


class Exoplanet(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.OneToOneField(AstronomicalCoordinates, null=True, blank=True)
    parent_star = models.ForeignKey('AstronomicalObject', null=True, blank=True, related_name="planets")
    discovery_date = models.DateField(null=True, blank=True)
    last_update = models.DateField(null=True, blank=True)

    mass = models.OneToOneField(Mass, null=True, blank=True)
    radius = models.OneToOneField(Radius, null=True, blank=True)
    inclination = models.OneToOneField(Angle, null=True, blank=True, related_name="inclination")
    molecules_detected = models.CharField(max_length=100)

    semimajor_axis = models.OneToOneField(EllipseAxis, null=True, blank=True, related_name="semimajor_axis")
    orbital_period = models.OneToOneField(Period, null=True, blank=True)
    eccentricity = models.OneToOneField(Eccentricity, null=True, blank=True)
    omega = models.OneToOneField(Angle, null=True, blank=True, related_name="omega")
    time_periastron = models.OneToOneField(JulianDay, null=True, blank=True, related_name="time_periastron")

    primary_transit = models.OneToOneField(JulianDay, null=True, blank=True, related_name="primary_transit")
    secondary_transit = models.OneToOneField(JulianDay, null=True, blank=True, related_name="secondary_transit")
    anomaly_angle = models.OneToOneField(Angle, null=True, blank=True, related_name="anomaly_angle")
    impact_parameter_b = models.OneToOneField(Angle, null=True, blank=True, related_name="impact_parameter_b")
    time_vr0 = models.OneToOneField(JulianDay, null=True, blank=True, related_name="time_vr0")
    velocity_semiamplitude_K = models.OneToOneField(Velocity, null=True, blank=True)

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

    DETECTION_METHOD_CHOICES = (
        (DETECTION_METHOD_UNKNOWN, 'unknown'),
        (DETECTION_METHOD_RV, 'radial velocities'),
        (DETECTION_METHOD_MICROLENSING, 'microlensing'),
        (DETECTION_METHOD_TRANSIT, 'transit'),
        (DETECTION_METHOD_TIMING, 'timing'),
        (DETECTION_METHOD_ASTROMETRY, 'astrometry'),
        (DETECTION_METHOD_IMAGING, 'imaging'),
    )

    detection_method = models.CharField(max_length=3, blank=True, choices=DETECTION_METHOD_CHOICES, default=DETECTION_METHOD_UNKNOWN)
    mass_detection_method = models.CharField(max_length=3, blank=True, choices=DETECTION_METHOD_CHOICES, default=DETECTION_METHOD_UNKNOWN)
    radius_detection_method = models.CharField(max_length=3, blank=True, choices=DETECTION_METHOD_CHOICES, default=DETECTION_METHOD_UNKNOWN)


class AstronomicalObject(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.OneToOneField(AstronomicalCoordinates, null=True, blank=True)
    mass = models.OneToOneField(Mass, null=True, blank=True)
