
from django.core import exceptions

from rest_framework import views
from rest_framework import response

from project.arcsecond import serializers
from project.arcsecond import models
from project.arcsecond import mixins

from astropy import coordinates as c
from astropy import units as u
from astropy import time as t

class CoordinatesConverterDetailAPIView(mixins.RequestLogViewMixin, views.APIView):

    def get(self, request, ra, dec, frame='icrs', format=None):
        coords = c.SkyCoord(ra, dec, frame=frame.lower(), unit=(u.hourangle, u.deg))

        conversion = models.CoordinatesConversion()
        conversion.input_first_value = ra
        conversion.input_second_value = dec
        conversion.input_frame = frame

        coords_CIRS = models.CIRSCoordinates(ra_unit='degrees', dec_unit='degrees')
        coords_CIRS.ra = str(coords.cirs.ra.deg)
        coords_CIRS.dec = str(coords.cirs.dec.deg)
        coords_CIRS.documentation = "A coordinate or frame in the Celestial Intermediate Reference System (CIRS)."
        coords_CIRS.documentation_URL = "http://docs.astropy.org/en/stable/api/astropy.coordinates.CIRS.html"
        coords_CIRS.save()

        coords_FK4 = models.FK4Coordinates(ra_unit='degrees', dec_unit='degrees')
        coords_FK4.ra = str(coords.fk4.ra.deg)
        coords_FK4.dec = str(coords.fk4.dec.deg)
        coords_FK4.equinox = str(coords.fk4.equinox)
        coords_FK4.documentation = "A coordinate or frame in the FK4 system."
        coords_FK4.documentation_URL = "http://docs.astropy.org/en/stable/api/astropy.coordinates.FK4.html"
        coords_FK4.save()

        coords_FK4NoETerms = models.FK4NoETermsCoordinates(ra_unit='degrees', dec_unit='degrees')
        coords_FK4NoETerms.ra = str(coords.fk4noeterms.ra.deg)
        coords_FK4NoETerms.dec = str(coords.fk4noeterms.dec.deg)
        coords_FK4NoETerms.equinox = str(coords.fk4.equinox)
        coords_FK4NoETerms.documentation = "A coordinate or frame in the FK4 system, but with the E-terms of aberration removed."
        coords_FK4NoETerms.documentation_URL = "http://docs.astropy.org/en/stable/api/astropy.coordinates.FK4.html"
        coords_FK4NoETerms.save()

        coords_FK5 = models.FK5Coordinates(ra_unit='degrees', dec_unit='degrees')
        coords_FK5.ra = str(coords.fk5.ra.deg)
        coords_FK5.dec = str(coords.fk5.dec.deg)
        coords_FK5.equinox = str(coords.fk4.equinox)
        coords_FK5.documentation = "A coordinate or frame in the FK5 system."
        coords_FK5.documentation_URL = "http://docs.astropy.org/en/stable/api/astropy.coordinates.FK4.html"
        coords_FK5.save()

        coords_GCRS = models.GCRSCoordinates(ra_unit='degrees', dec_unit='degrees')
        coords_GCRS.ra = str(coords.gcrs.ra.deg)
        coords_GCRS.dec = str(coords.gcrs.dec.deg)
        coords_GCRS.documentation = "A coordinate or frame in the Geocentric Celestial Reference System (GCRS). GCRS is distinct form ICRS mainly in that it is relative to the EarthGalactics center-of-mass rather than the solar system Barycenter. That means this frame includes the effects of abberation (unlike ICRS). This frame also includes frames that are defined relative to the Earth, but that are offset (in both position and velocity) from the Earth."
        coords_GCRS.documentation_URL = "http://docs.astropy.org/en/stable/api/astropy.coordinates.GCRS.html"
        coords_GCRS.save()

        coords_Galactic = models.GalacticCoordinates(l_unit='degrees', b_unit='degrees')
        coords_Galactic.l = str(coords.galactic.l.deg)
        coords_Galactic.b = str(coords.galactic.b.deg)
        coords_Galactic.documentation = "Galactic Coordinates."
        coords_Galactic.documentation_URL = "http://docs.astropy.org/en/stable/api/astropy.coordinates.Galactic.html"
        coords_Galactic.save()

        coords_ICRS = models.ICRSCoordinates(ra_unit='degrees', dec_unit='degrees')
        coords_ICRS.ra = str(coords.icrs.ra.deg)
        coords_ICRS.dec = str(coords.icrs.dec.deg)
        coords_ICRS.documentation = "A coordinate or frame in the ICRS system. If you're looking for 'J2000' coordinates, and aren't sure if you want to use this or FK5, you probably want to use ICRS. It's more well-defined as a catalog coordinate and is an inertial system, and is very close (within tens of milliarcseconds) to J2000 equatorial."
        coords_ICRS.documentation_URL = "http://docs.astropy.org/en/stable/api/astropy.coordinates.ICRS.html"
        coords_ICRS.save()

        conversion.CIRS = coords_CIRS
        conversion.FK4 = coords_FK4
        conversion.FK4noETerms = coords_FK4NoETerms
        conversion.FK5 = coords_FK5
        conversion.GCRS = coords_GCRS
        conversion.Galactic = coords_Galactic
        conversion.ICRS = coords_ICRS
        conversion.save()

        serializer = serializers.CoordinatesConversionSerializer(conversion)
        return response.Response(serializer.data)


class TimesDetailAPIView(mixins.RequestLogViewMixin, views.APIView):
    def get(self, request, input_format, input_value, format=None):

        conversion = models.TimesConversion()
        conversion.input_format = input_format
        conversion.input_value = input_value
        conversion.documentation_URL = "http://docs.astropy.org/en/stable/time/index.html#reference-api"

        if input_format in ['byear', 'cxcsec', 'decimalyear', 'gps', 'jd', 'jyear', 'mjd', 'plot_date', 'unix']:
            input_value = float(input_value)

        try:
            time = t.Time(input_value, format=input_format)
        except ValueError as e:
            conversion_error = models.Error(code=9, message=e.message)
            conversion_error.save()
            conversion.error = conversion_error
        else:
            conversion.byear = time.byear
            conversion.byear_str = time.byear_str
            conversion.cxcsec = time.cxcsec

            try:
                conversion.datetime = time.datetime
            except ValueError as datetime_e:
                if conversion.error is None:
                    conversion_error = models.Error(code=9, message='datetime: '+datetime_e.message)
                    conversion_error.save()
                    conversion.error = conversion_error
                else:
                    conversion.error.message += ", datetime: "+datetime_e.message
                    conversion.error.save()

            conversion.decimalyear = time.decimalyear
            conversion.gps = time.gps
            conversion.iso = time.iso
            conversion.isot = time.isot
            conversion.jd = time.jd
            conversion.jyear = time.jyear
            conversion.jyear_str = time.jyear_str
            conversion.mjd = time.mjd
            conversion.plot_date = time.plot_date
            conversion.unix = time.unix

            try:
                conversion.yday = time.yday
            except ValueError as datetime_e:
                if conversion.error is None:
                    conversion_error = models.Error(code=9, message='yday: '+datetime_e.message)
                    conversion_error.save()
                    conversion.error = conversion_error
                else:
                    conversion.error.message += ", yday: "+datetime_e.message
                    conversion.error.save()

        serializer = serializers.TimesConversionSerializer(conversion)
        return response.Response(serializer.data)
