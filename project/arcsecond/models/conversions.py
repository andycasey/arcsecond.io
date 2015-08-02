from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models

from .sky import AstronomicalCoordinates

class CoordinatesConversion(models.Model):
    class Meta: app_label = 'arcsecond'

    input_coordinates = models.OneToOneField(AstronomicalCoordinates, null=True, blank=True)
