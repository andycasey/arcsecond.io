
from django.db import models
from .constants import *

# class AltAzCoordinates(models.Model):
#     az = models.CharField(max_length=20, null=True, blank=True)
#     az_unit = models.CharField(max_length=20, null=True, blank=True)
#     alt = models.CharField(max_length=20, null=True, blank=True)
#     alt_unit = models.CharField(max_length=20, null=True, blank=True)
#     documentation = models.URLField(max_length=200, null=True, blank=True)
#
# class GalactocentricCoordinates(models.Model):
#     galcen_ra = models.CharField(max_length=20, null=True, blank=True)
#     galcen_dec = models.CharField(max_length=20, null=True, blank=True)
#     z_sun = models.CharField(max_length=20, null=True, blank=True)
#     z_sun_unit = models.CharField(max_length=20, null=True, blank=True)
#     roll = models.CharField(max_length=20, null=True, blank=True)
#     documentation = models.URLField(max_length=200, null=True, blank=True)
#
# class ITRSCoordinates(models.Model):
#     pass
#

class CIRSCoordinates(models.Model):
    ra = models.CharField(max_length=20, null=True, blank=True)
    ra_unit = models.CharField(max_length=20, null=True, blank=True)
    dec = models.CharField(max_length=20, null=True, blank=True)
    dec_unit = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    distance_unit = models.CharField(max_length=20, null=True, blank=True)
    documentation = models.CharField(max_length=1000, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)

class FK4Coordinates(models.Model):
    ra = models.CharField(max_length=20, null=True, blank=True)
    ra_unit = models.CharField(max_length=20, null=True, blank=True)
    dec = models.CharField(max_length=20, null=True, blank=True)
    dec_unit = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    distance_unit = models.CharField(max_length=20, null=True, blank=True)
    equinox = models.CharField(max_length=20, null=True, blank=True)
    documentation = models.CharField(max_length=1000, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)

class FK4NoETermsCoordinates(models.Model):
    ra = models.CharField(max_length=20, null=True, blank=True)
    ra_unit = models.CharField(max_length=20, null=True, blank=True)
    dec = models.CharField(max_length=20, null=True, blank=True)
    dec_unit = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    distance_unit = models.CharField(max_length=20, null=True, blank=True)
    equinox = models.CharField(max_length=20, null=True, blank=True)
    documentation = models.CharField(max_length=1000, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)

class FK5Coordinates(models.Model):
    ra = models.CharField(max_length=20, null=True, blank=True)
    ra_unit = models.CharField(max_length=20, null=True, blank=True)
    dec = models.CharField(max_length=20, null=True, blank=True)
    dec_unit = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    distance_unit = models.CharField(max_length=20, null=True, blank=True)
    equinox = models.CharField(max_length=20, null=True, blank=True)
    documentation = models.CharField(max_length=1000, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)

class GCRSCoordinates(models.Model):
    ra = models.CharField(max_length=20, null=True, blank=True)
    ra_unit = models.CharField(max_length=20, null=True, blank=True)
    dec = models.CharField(max_length=20, null=True, blank=True)
    dec_unit = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    distance_unit = models.CharField(max_length=20, null=True, blank=True)
    documentation = models.CharField(max_length=1000, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)

class GalacticCoordinates(models.Model):
    l = models.CharField(max_length=20, null=True, blank=True)
    l_unit = models.CharField(max_length=20, null=True, blank=True)
    b = models.CharField(max_length=20, null=True, blank=True)
    b_unit = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    distance_unit = models.CharField(max_length=20, null=True, blank=True)
    documentation = models.CharField(max_length=1000, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)

class ICRSCoordinates(models.Model):
    ra = models.CharField(max_length=20, null=True, blank=True)
    ra_unit = models.CharField(max_length=20, null=True, blank=True)
    dec = models.CharField(max_length=20, null=True, blank=True)
    dec_unit = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    distance_unit = models.CharField(max_length=20, null=True, blank=True)
    documentation = models.CharField(max_length=1000, null=True, blank=True)
    documentation_URL = models.URLField(max_length=200, null=True, blank=True)


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

    right_ascension = models.FloatField(null=True, blank=True)
    right_ascension_units = models.CharField(max_length=100, default='degrees')

    declination = models.FloatField(null=True, blank=True)
    declination_units = models.CharField(max_length=100, default='degrees')

    epoch = models.FloatField(default=J2000)
    equinox = models.FloatField(default=J2000)

    def are_empty(self):
        return self.right_ascension == NOT_A_SCIENTIFIC_NUMBER or \
               self.declination == NOT_A_SCIENTIFIC_NUMBER or \
               self.epoch == NOT_A_SCIENTIFIC_NUMBER

    def __unicode__(self):
        return u"(R.A.: %.8f, Dec: %.8f, epoch: %.2f, equinox: %.2f)"%(self.right_ascension, self.declination, self.epoch, self.equinox)

