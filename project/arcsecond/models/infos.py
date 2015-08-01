# -*- coding: utf-8 -*-

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
    MASS_JUPITER = "jup"
    MASS_NEPTUNE = "nep"
    MASS_EARTH = "ear"

    MASSES_KEYS = (MASS_SUN, MASS_JUPITER, MASS_NEPTUNE, MASS_EARTH)
    MASSES_VALUES = ('Sun', 'Jupiter', 'Neptune', 'Earth')
    MASSES_CHOICES = tuple(zip(MASSES_KEYS, MASSES_VALUES))

    unit = models.CharField(max_length=3, choices=MASSES_CHOICES, default=MASS_SUN)

class Radius(AstronomicalInfo):
    RADIUS_SUN = "sun"
    RADIUS_JUPITER = "jup"
    RADIUS_NEPTUNE = "nep"
    RADIUS_EARTH = "ear"

    RADIUS_KEYS = (RADIUS_SUN, RADIUS_JUPITER, RADIUS_NEPTUNE, RADIUS_EARTH)
    RADIUS_VALUES =  ('Sun', 'Jupiter', 'Neptune', 'Earth')
    RADIUS_CHOICES = tuple(zip(RADIUS_KEYS, RADIUS_VALUES))

    unit = models.CharField(max_length=3, choices=RADIUS_CHOICES, default=RADIUS_SUN)

class Age(AstronomicalInfo):
    AGE_GYR = "Gyr"
    AGE_MYR = "Myr"
    AGE_YR = "yr"

    AGE_KEYS = (AGE_GYR, AGE_MYR, AGE_YR)
    AGE_VALUES = ('Gyr', 'Myr', 'yr')
    AGE_CHOICES = tuple(zip(AGE_KEYS, AGE_VALUES))

    unit = models.CharField(max_length=3, choices=AGE_CHOICES, default=AGE_GYR)

class Temperature(AstronomicalInfo):
    TEMP_KELVIN = "K"
    TEMP_CELSIUS = "C"

    TEMP_KEYS = (TEMP_KELVIN, TEMP_CELSIUS)
    TEMP_VALUES = ('Kelvin', 'Celsius')
    TEMP_CHOICES = tuple(zip(TEMP_KEYS, TEMP_VALUES))

    unit = models.CharField(max_length=1, choices=TEMP_CHOICES, default=TEMP_KELVIN)

class Metallicity(AstronomicalInfo):
    METAL_Z = "Z"
    METAL_FEH = "F"

    METAL_KEYS = (METAL_Z, METAL_FEH)
    METAL_VALUES = ('Z', 'Fe/H')
    METAL_CHOICES = tuple(zip(METAL_KEYS, METAL_VALUES))

    unit = models.CharField(max_length=1, choices=METAL_CHOICES, default=METAL_Z)


class Distance(AstronomicalInfo):
    DISTANCE_KM = "km"
    DISTANCE_UA = "UA"
    DISTANCE_LY = "ly"
    DISTANCE_PC = "pc"
    DISTANCE_KPC = "kpc"
    DISTANCE_MPC = "Mpc"

    DISTANCE_KEYS = (DISTANCE_KM, DISTANCE_UA, DISTANCE_LY, DISTANCE_PC, DISTANCE_KPC, DISTANCE_MPC)
    DISTANCE_VALUES = ('km', 'UA', 'ly', 'pc', 'kpc', 'Mpc')
    DISTANCE_CHOICES = tuple(zip(DISTANCE_KEYS, DISTANCE_VALUES))

    unit = models.CharField(max_length=3, choices=DISTANCE_CHOICES, default=DISTANCE_PC)


class Period(AstronomicalInfo):
    PERIOD_SECOND = "s"
    PERIOD_MINUTE = "m"
    PERIOD_DAY = "d"
    PERIOD_HOUR = "h"
    PERIOD_WEEK = "w"
    PERIOD_YEAR = "y"

    PERIOD_KEYS = (PERIOD_SECOND, PERIOD_MINUTE, PERIOD_DAY, PERIOD_HOUR, PERIOD_WEEK, PERIOD_YEAR)
    PERIOD_VALUES = ('seconds', 'minutes', 'days', 'hours', 'weeks', 'years')
    PERIOD_CHOICES = tuple(zip(PERIOD_KEYS, PERIOD_VALUES))

    unit = models.CharField(max_length=1, choices=PERIOD_CHOICES, default=PERIOD_DAY)

class EllipseAxis(AstronomicalInfo):
    AXIS_UA = "astronomical unit"
    AXIS_SUN = "sun radius"

    AXIS_KEYS = (AXIS_UA, AXIS_SUN)
    AXIS_VALUES = ('astronomical unit', 'sun radius')
    AXIS_CHOICES = tuple(zip(AXIS_KEYS, AXIS_VALUES))

    unit = models.CharField(max_length=18, choices=AXIS_CHOICES, default=AXIS_UA)


class Angle(AstronomicalInfo):
    ANGLE_MILIARCSEC = "mas"
    ANGLE_ARCSEC = "sec"
    ANGLE_ARCMIN = "min"
    ANGLE_DEGREE = "deg"

    ANGLE_KEYS = (ANGLE_MILIARCSEC, ANGLE_ARCSEC, ANGLE_ARCMIN, ANGLE_DEGREE)
    ANGLE_VALUES = ("mas", "'", "\"", u"º")
    ANGLE_CHOICES = tuple(zip(ANGLE_KEYS, ANGLE_VALUES))

    unit = models.CharField(max_length=3, choices=ANGLE_CHOICES, default=ANGLE_ARCSEC)

class Velocity(AstronomicalInfo):
    unit = models.CharField(max_length=10, default="m/s")

class Gravity(AstronomicalInfo):
    unit = models.CharField(max_length=10, default="log(g/gH)")

