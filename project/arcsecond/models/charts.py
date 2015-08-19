__author__ = 'onekiloparsec'

from django.db import models

class FindingChart(models.Model):
    class Meta: app_label = 'arcsecond'

    input = models.CharField(max_length=100, null=True, blank=True)

    SURVEY_NAME_UNDEFINED = "unk"
    SURVEY_NAME_SDSS = "sdss"
    SURVEY_NAME_DSS = "dss"
    SURVEY_NAME_TWOMASS = "2mass"

    SURVEY_NAME_KEYS = (
        SURVEY_NAME_UNDEFINED,
        SURVEY_NAME_SDSS,
        SURVEY_NAME_DSS,
        SURVEY_NAME_TWOMASS,
    )

    SURVEY_NAME_VALUES = (
        '(Undefined)',
        'SDSS',
        'DSS',
        '2MASS',
    )

    SURVEY_NAME_CHOICES = tuple(zip(SURVEY_NAME_KEYS, SURVEY_NAME_VALUES))
    survey_name = models.CharField(max_length=20, choices=SURVEY_NAME_CHOICES, default=SURVEY_NAME_UNDEFINED)

    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    SIZE_UNIT_UNDEFINED = "unk"
    SIZE_UNIT_ARCSECONDS = "arcsec"
    SIZE_UNIT_ARCMINUTES = "arcmin"
    SIZE_UNIT_DEGREES = "deg"

    SIZE_UNIT_KEYS = (
        SIZE_UNIT_UNDEFINED,
        SIZE_UNIT_ARCSECONDS,
        SIZE_UNIT_ARCMINUTES,
        SIZE_UNIT_DEGREES
    )

    SIZE_UNIT_VALUES = (
        '(Undefined)',
        'arcseconds',
        'arcminutes',
        'degrees',
    )

    SIZE_UNIT_CHOICES = tuple(zip(SIZE_UNIT_KEYS, SIZE_UNIT_VALUES))
    size_unit = models.CharField(max_length=20, choices=SIZE_UNIT_CHOICES, default=SIZE_UNIT_UNDEFINED)

    ORIENTATION_UNDEFINED = "unk"
    ORIENTATION_NORTHUP_EASTLEFT = "NuEl"
    ORIENTATION_NORTHUP_EASTRIGHT = "NuEr"
    ORIENTATION_NORTHDOWN_EASTLEFT = "NdEl"
    ORIENTATION_NORTHDOWN_EASTRIGHT = "NdEr"

    ORIENTATION_KEYS = (
        ORIENTATION_UNDEFINED,
        ORIENTATION_NORTHUP_EASTLEFT,
        ORIENTATION_NORTHUP_EASTRIGHT,
        ORIENTATION_NORTHDOWN_EASTLEFT,
        ORIENTATION_NORTHDOWN_EASTRIGHT
    )

    ORIENTATION_VALUES = (
        '(Undefined)',
        'N up E left',
        'N up E right',
        'N down E left',
        'N down E right',
    )

    ORIENTATION_CHOICES = tuple(zip(ORIENTATION_KEYS, ORIENTATION_VALUES))
    orientation = models.CharField(max_length=20, choices=ORIENTATION_CHOICES, default=ORIENTATION_UNDEFINED)

    band_name = models.CharField(max_length=20, null=True, blank=True)
    observing_date = models.DateField(null=True, blank=True)

    fits_url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500)
