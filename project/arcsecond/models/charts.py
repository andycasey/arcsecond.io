__author__ = 'onekiloparsec'

from django.db import models

class FindingChart(models.Model):
    class Meta: app_label = 'arcsecond'

    input = models.CharField(max_length=100, null=True, blank=True)

    SURVEY_NAME_UNDEFINED = "(Undefined)"
    SURVEY_NAME_SDSS = "SDSS"
    SURVEY_NAME_DSS = "SDSS"
    SURVEY_NAME_TWOMASS = "2MASS"

    SURVEY_NAME_CHOICES = (
        (SURVEY_NAME_UNDEFINED, '(Undefined)'),
        (SURVEY_NAME_SDSS, 'SDSS'),
        (SURVEY_NAME_DSS, 'SDSS'),
        (SURVEY_NAME_TWOMASS, '2MASS'),
    )

    survey_name = models.CharField(max_length=20, choices=SURVEY_NAME_CHOICES, default=SURVEY_NAME_UNDEFINED)

    width = models.SmallIntegerField(null=True, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)

    SIZE_UNIT_UNDEFINED = "(Undefined)"
    SIZE_UNIT_ARCSECONDS = "arcsec"
    SIZE_UNIT_ARCMINUTES = "arcmin"
    SIZE_UNIT_DEGREES = "deg"

    SIZE_UNIT_CHOICES = (
        (SIZE_UNIT_UNDEFINED, '(Undefined)'),
        (SIZE_UNIT_ARCSECONDS, 'arcsec'),
        (SIZE_UNIT_ARCMINUTES, 'arcmin'),
        (SIZE_UNIT_DEGREES, 'deg'),
    )

    size_unit = models.CharField(max_length=20, choices=SIZE_UNIT_CHOICES, default=SIZE_UNIT_UNDEFINED)

    ORIENTATION_UNDEFINED = "(Undefined)"
    ORIENTATION_NORTHUP_EASTLEFT = "N up E left"
    ORIENTATION_NORTHUP_EASTRIGHT = "N up E right"
    ORIENTATION_NORTHDOWN_EASTLEFT = "N down E left"
    ORIENTATION_NORTHDOWN_EASTRIGHT = "N down E right"

    ORIENTATION_CHOICES = (
        (ORIENTATION_UNDEFINED, '(Undefined)'),
        (ORIENTATION_NORTHUP_EASTLEFT, 'N up E left'),
        (ORIENTATION_NORTHUP_EASTRIGHT, 'N up E right'),
        (ORIENTATION_NORTHDOWN_EASTLEFT, 'N down E left'),
        (ORIENTATION_NORTHDOWN_EASTRIGHT, 'N down E right'),
    )

    orientation = models.CharField(max_length=20, choices=ORIENTATION_CHOICES, default=ORIENTATION_UNDEFINED)

    band_name = models.CharField(max_length=20, null=True, blank=True)
    fits_url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500)
    observing_date = models.DateField(null=True, blank=True)
