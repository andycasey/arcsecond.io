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
