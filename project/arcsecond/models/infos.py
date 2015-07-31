from django.core.validators import RegexValidator
from django.db import models
from .constants import *

import math

class AstronomicalInfo(models.Model):
    class Meta: abstract = True

    value = models.FloatField(null=True, blank=True)
    error = models.FloatField(null=True, blank=True)
    error_max = models.FloatField(null=True, blank=True)
    error_min = models.FloatField(null=True, blank=True)
    bibcode = models.CharField(max_length=50, default="", null=True, blank=True, validators=[RegexValidator(regex=bibcode_regex, message='Invalid bibcode', code='nomatch')])


class JulianDay(AstronomicalInfo):
    pass

class Albedo(AstronomicalInfo):
    pass

class Eccentricity(AstronomicalInfo):
    pass

class Flux(AstronomicalInfo):
    name = models.CharField(max_length=500)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="fluxes", blank=True)

    # see https://docs.djangoproject.com/en/1.6/topics/db/models/#model-methods
    def is_valid(self):
        return len(self.name) > 0 and not math.isnan(self.value)


class Color(AstronomicalInfo):
    first_magnitude_name = models.CharField(max_length=2)
    second_magnitude_name = models.CharField(max_length=2)


class Mass(AstronomicalInfo):
    MASS_SUN = "sun"
    MASS_JUPITER = "jupiter"
    MASS_NEPTUNE = "neptune"
    MASS_EARTH = "earth"

    MASSES_CHOICES = (
        (MASS_SUN, 'Sun'),
        (MASS_JUPITER, 'Jupiter'),
        (MASS_NEPTUNE, 'Neptune'),
        (MASS_EARTH, 'Earth'),
    )

    unit = models.CharField(max_length=7, choices=MASSES_CHOICES, default=MASS_SUN)

class Radius(AstronomicalInfo):
    RADIUS_SUN = "sun"
    RADIUS_JUPITER = "jupiter"
    RADIUS_NEPTUNE = "neptune"
    RADIUS_EARTH = "earth"

    RADIUS_CHOICES = (
        (RADIUS_SUN, 'Sun'),
        (RADIUS_JUPITER, 'Jupiter'),
        (RADIUS_NEPTUNE, 'Neptune'),
        (RADIUS_EARTH, 'Earth'),
    )

    unit = models.CharField(max_length=7, choices=RADIUS_CHOICES, default=RADIUS_SUN)

class Age(AstronomicalInfo):
    AGE_GYR = "Gyr"
    AGE_MYR = "Myr"
    AGE_YR = "yr"

    AGE_CHOICES = (
        (AGE_GYR, 'Gyr'),
        (AGE_MYR, 'Myr'),
        (AGE_YR, 'yr'),
    )

    unit = models.CharField(max_length=3, choices=AGE_CHOICES, default=AGE_GYR)

class Temperature(AstronomicalInfo):
    TEMP_KELVIN = "K"
    TEMP_CELSIUS = "C"

    TEMP_CHOICES = (
        (TEMP_KELVIN, 'Kelvin'),
        (TEMP_CELSIUS, 'Celsius'),
    )

    unit = models.CharField(max_length=1, choices=TEMP_CHOICES, default=TEMP_KELVIN)

class Metallicity(AstronomicalInfo):
    METAL_Z = "Z"
    METAL_FEH = "F"

    METAL_CHOICES = (
        (METAL_Z, 'Z'),
        (METAL_FEH, 'Fe/H'),
    )

    unit = models.CharField(max_length=4, choices=METAL_CHOICES, default=METAL_Z)


class Distance(AstronomicalInfo):
    DISTANCE_KM = "km"
    DISTANCE_UA = "UA"
    DISTANCE_LY = "ly"
    DISTANCE_PC = "pc"
    DISTANCE_KPC = "kpc"
    DISTANCE_MPC = "Mpc"

    DISTANCE_CHOICES = (
        (DISTANCE_KM, 'km'),
        (DISTANCE_UA, 'UA'),
        (DISTANCE_LY, 'ly'),
        (DISTANCE_PC, 'pc'),
        (DISTANCE_KPC, 'kpc'),
        (DISTANCE_MPC, 'Mpc'),
    )

    unit = models.CharField(max_length=3, choices=DISTANCE_CHOICES, default=DISTANCE_PC)


class Period(AstronomicalInfo):
    OPERIOD_SECOND = "s"
    OPERIOD_MINUTE = "m"
    OPERIOD_DAY = "d"
    OPERIOD_HOUR = "h"
    OPERIOD_WEEK = "w"
    OPERIOD_YEAR = "y"

    OPERIOD_CHOICES = (
        (OPERIOD_SECOND, 'seconds'),
        (OPERIOD_MINUTE, 'minutes'),
        (OPERIOD_DAY, 'days'),
        (OPERIOD_HOUR, 'hours'),
        (OPERIOD_WEEK, 'weeks'),
        (OPERIOD_YEAR, 'years'),
    )

    unit = models.CharField(max_length=1, choices=OPERIOD_CHOICES, default=OPERIOD_DAY)

class EllipseAxis(AstronomicalInfo):
    AXIS_UA = "astronomical unit"
    AXIS_SUN = "sun radius"

    AXIS_CHOICES = (
        (AXIS_UA, 'astronomical unit'),
        (AXIS_SUN, 'sun radius'),
    )

    unit = models.CharField(max_length=18, choices=AXIS_CHOICES, default=AXIS_UA)

class AngularDistance(AstronomicalInfo):
    ANG_DISTANCE_ARCSEC = "arcsec"
    ANG_DISTANCE_ARCMIN = "arcmin"

    ANG_DISTANCE_CHOICES = (
        (ANG_DISTANCE_ARCSEC, 'arcsec'),
        (ANG_DISTANCE_ARCMIN, 'arcmin'),
    )

    unit = models.CharField(max_length=6, choices=ANG_DISTANCE_CHOICES, default=ANG_DISTANCE_ARCSEC)


class Angle(AstronomicalInfo):
    unit = models.CharField(max_length=10, default="degrees")

class Velocity(AstronomicalInfo):
    unit = models.CharField(max_length=10, default="m/s")

class Gravity(AstronomicalInfo):
    unit = models.CharField(max_length=10, default="log(g/gH)")

class Parallax(AstronomicalInfo):
    unit = models.CharField(max_length=3, default="mas")