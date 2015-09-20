
from django.db import models
from .constants import *

# **** ASTROPY COMPATIBILITY: 1.0 **** #

class CoordinatesManager(models.Manager):
    def get_by_natural_key(self, longitude, latitude):
        return self.get(longitude=longitude, latitude=latitude)

class Coordinates(models.Model):
    """The minimal set of 3D values to define a location coordinates on Earth.
    See http://docs.astropy.org/en/stable/api/astropy.coordinates.Coordinates.html
    """
    class Meta:
        app_label = 'arcsecond'
        unique_together = (('longitude', 'latitude'),)
        ordering = ["longitude", "latitude"]

    objects = CoordinatesManager()

    longitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    latitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    height = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)

    def natural_key(self):
        return (self.longitude, self.latitude)

    def are_empty(self):
        return self.longitude == NOT_A_SCIENTIFIC_NUMBER or \
               self.latitude == NOT_A_SCIENTIFIC_NUMBER or \
               self.height == NOT_A_SCIENTIFIC_NUMBER

    def __unicode__(self):
        return u"(long: %.8f, lat: %.8f, h: %.2fm)" % (self.longitude, self.latitude, self.height)

