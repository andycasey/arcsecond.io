from rest_framework import serializers
from project.arcsecond.models import CoordinatesConversion, TimesConversion, Error
from .coordinates import *

######################## Conversions ########################

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ('code', 'message')

class CoordinatesConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatesConversion
        fields = ('input_first_value', 'input_second_value', 'input_frame', 'error',
                  'CIRS', 'FK4', 'FK4NoETerms', 'FK5', 'GCRS', 'Galactic', 'ICRS')

    error = ErrorSerializer(required=False)

    CIRS = CIRSCoordinatesSerializer(required=False)
    FK4 = FK4CoordinatesSerializer(required=False)
    FK4NoETerms = FK4NoETermsCoordinatesSerializer(required=False)
    FK5 = FK5CoordinatesSerializer(required=False)
    GCRS = GCRSCoordinatesSerializer(required=False)
    Galactic = GalacticCoordinatesSerializer(required=False)
    ICRS = ICRSCoordinatesSerializer(required=False)


class TimesConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimesConversion
        fields = ('input_format', 'input_value', 'documentation_URL', 'error', 'byear', 'byear_str', 'cxcsec', 'datetime',
                  'decimalyear', 'gps', 'iso', 'isot', 'jd', 'jyear', 'jyear_str', 'mjd', 'plot_date', 'unix', 'yday')

    error = ErrorSerializer(required=False)

