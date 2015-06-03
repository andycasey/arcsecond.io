
from django.db import models
from .constants import *

import math

class AstronomicalCoordinates(models.Model):
    class Meta: app_label = 'iobserve'

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
    class Meta: app_label = 'iobserve'

    name = models.CharField(max_length=500)
    catalogue_url = models.URLField(null=True)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="aliases", blank=True)


class ObjectType(models.Model):
    class Meta: app_label = 'iobserve'

    value = models.CharField(max_length=500)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="object_types", blank=True)


class AstronomicalFlux(models.Model):
    class Meta: app_label = 'iobserve'

    name = models.CharField(max_length=500)
    value = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    error_value = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    bibcode = models.CharField(max_length=500, null=True, blank=True)
    unit = models.CharField(max_length=500, null=True, blank=True)
    astronomical_object = models.ForeignKey('AstronomicalObject', null=True, related_name="fluxes", blank=True)

    # see https://docs.djangoproject.com/en/1.6/topics/db/models/#model-methods
    def is_valid(self):
        return len(self.name) > 0 and not math.isnan(self.value)


class AstronomicalObject(models.Model):
    class Meta: app_label = 'iobserve'

    name = models.CharField(max_length=100)
    coordinates = models.OneToOneField(AstronomicalCoordinates, null=True)



