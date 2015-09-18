from rest_framework import serializers
from project.arcsecond.models.coordinates import *

class AstronomicalCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomicalCoordinates
        fields = ("system", "right_ascension", "right_ascension_units", "declination", "declination_units", "epoch", "equinox")

######################## Coordinates ########################

class CIRSCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CIRSCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'documentation', 'documentation_URL')

class FK4CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FK4Coordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'equinox', 'documentation', 'documentation_URL')

class FK4NoETermsCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FK4NoETermsCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'equinox', 'documentation', 'documentation_URL')

class FK5CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FK5Coordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'equinox', 'documentation', 'documentation_URL')

class GCRSCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCRSCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'documentation', 'documentation_URL')

class GalacticCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalacticCoordinates
        fields = ('l', 'l_unit', 'b', 'b_unit', 'documentation', 'documentation_URL')

class ICRSCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICRSCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'documentation', 'documentation_URL')


