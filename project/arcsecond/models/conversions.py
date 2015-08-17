from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models
from .coordinates import *

class CoordinatesConversion(models.Model):
    class Meta: app_label = 'arcsecond'

    input_first_value = models.CharField(max_length=20, null=True, blank=True)
    input_second_value = models.CharField(max_length=20, null=True, blank=True)
    input_frame = models.CharField(max_length=20, null=True, blank=True)

    CIRS = models.OneToOneField(CIRSCoordinates, null=True, blank=True)
    FK4 = models.OneToOneField(FK4Coordinates, null=True, blank=True)
    FK4noETerms = models.OneToOneField(FK4NoETermsCoordinates, null=True, blank=True)
    FK5 = models.OneToOneField(FK5Coordinates, null=True, blank=True)
    GCRS = models.OneToOneField(GCRSCoordinates, null=True, blank=True)
    Galactic = models.OneToOneField(GalacticCoordinates, null=True, blank=True)
    ICRS = models.OneToOneField(ICRSCoordinates, null=True, blank=True)


class TimesConversion(models.Model):
    class Meta: app_label = 'arcsecond'

    input_format = models.CharField(max_length=100, null=True, blank=True)
    input_value = models.CharField(max_length=100, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)

    byear = models.FloatField(max_length=100, null=True, blank=True)
    byear_str = models.CharField(max_length=100, null=True, blank=True)
    cxcsec = models.FloatField(max_length=100, null=True, blank=True)
    datetime = models.CharField(max_length=100, null=True, blank=True)
    decimalyear = models.FloatField(max_length=100, null=True, blank=True)
    gps = models.FloatField(max_length=100, null=True, blank=True)
    iso = models.CharField(max_length=100, null=True, blank=True)
    isot = models.CharField(max_length=100, null=True, blank=True)
    jd = models.FloatField(max_length=100, null=True, blank=True)
    jyear = models.FloatField(max_length=100, null=True, blank=True)
    jyear_str = models.CharField(max_length=100, null=True, blank=True)
    mjd = models.FloatField(max_length=100, null=True, blank=True)
    plot_date = models.FloatField(max_length=100, null=True, blank=True)
    unix = models.FloatField(max_length=100, null=True, blank=True)
    yday = models.CharField(max_length=100, null=True, blank=True)


