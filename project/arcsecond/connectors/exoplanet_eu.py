import string
import urllib2
import math
from rest_framework import status
from project.arcsecond.models import *
from astropy.io import votable
from django.core.exceptions import MultipleObjectsReturned

EXOPLANET_EU_URL = "http://exoplanet.eu/catalog/votable/"
EXOPLANET_EU_URL_FORMAT = "http://exoplanet.eu/catalog/votable/?f=%22{}%22+in+name"

def get_EXOPLANET_EU_full_catalog():
    try:
        response = urllib2.urlopen(EXOPLANET_EU_URL)
    except urllib2.URLError:
        return None
    else:
        try:
            response_votable = votable.parse(response.fp)
            first_table = response_votable.get_first_table()
        except:
            return None
        else:

            for row in xrange(len(first_table.array)):
                name = first_table.array[row][0]

                try:
                    exoplanet, created = Exoplanet.objects.get_or_create(name=name)
                except MultipleObjectsReturned:
                    exoplanet = Exoplanet.objects.filter(name=name).first()

                last_field_name = "this_impossible_field_name"
                last_field_info = None

                for index, field in enumerate(first_table.fields):
                    if field.name == last_field_name+"_error_min" or field.name == last_field_name+"_error_max":
                        property_name = string.join(field.name.split("_")[-2:], "_")
                        try:
                            value = float(first_table.array[row][index])
                        except ValueError:
                            pass
                        else:
                            setattr(last_field_info, property_name, value)
                            last_field_info.save()

                    elif hasattr(exoplanet, field.name):
                        last_field_name = field.name

                        if field.name.capitalize() in globals():
                            field_class = globals()[field.name.capitalize()]
                            last_field_info = field_class()
                            if isinstance(last_field_info, AstronomicalInfo):
                                try:
                                    value = float(first_table.array[row][index])
                                except ValueError:
                                    pass
                                else:
                                    last_field_info.value = value
                                    last_field_info.save()
                                setattr(exoplanet, field.name, last_field_info)
                            else:
                                last_field_info = None

                    else:
                        last_field_name = "this_impossible_field_name"

                if exoplanet.mass is not None:
                    exoplanet.mass.unit = Mass.MASS_JUPITER
                    exoplanet.mass.save()
                if exoplanet.radius is not None:
                    exoplanet.radius.unit = Radius.RADIUS_JUPITER
                    exoplanet.radius.save()

                exoplanet.save()


def get_EXOPLANET_EU_object(name):
    url = EXOPLANET_EU_URL_FORMAT.format(urllib2.quote(name))

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return None
    else:
        try:
            response_votable = votable.parse(response.fp)
            first_table = response_votable.get_first_table()
        except:
            return None
        else:
            name = first_table.array[0][0]

            try:
                exoplanet, created = Exoplanet.objects.get_or_create(name=name)
            except MultipleObjectsReturned:
                exoplanet = Exoplanet.objects.filter(name=name).first()

            last_field_name = "this_impossible_field_name"
            last_field_info = None

            for index, field in enumerate(first_table.fields):
                if last_field_info is not None and field.name in [last_field_name+"_error_min", last_field_name+"_error_max"]:
                    error_name = string.join(field.name.split("_")[-2:], "_")
                    try:
                        value = float(first_table.array[0][index])
                    except ValueError:
                        pass
                    else:
                        if not math.isnan(value):
                            setattr(last_field_info, error_name, value)
                            last_field_info.save()

                elif hasattr(exoplanet, field.name):
                    last_field_name = field.name
                    last_field_info = None
                    field_instance = None

                    class_name = string.join([ sub.capitalize() for sub in field.name.split("_") ], "")

                    try:
                        value = float(first_table.array[0][index])
                    except ValueError:
                        pass
                    else:

                        if class_name in globals():
                            field_class = globals()[class_name]
                            field_instance = field_class()

                        elif last_field_name in ['inclination', 'omega', 'anomaly_angle', 'impact_parameter_b', 'hottest_point_longitude']:
                            field_instance = Angle()

                        elif last_field_name in ['semi_major_axis',]:
                            field_instance = EllipseAxis()

                        elif last_field_name in ['orbital_period',]:
                            field_instance = Period()

                        elif last_field_name in ['eccentricity',]:
                            field_instance = Period()

                        elif last_field_name in ['time_periastron', 'primary_transit', 'secondary_transit', 'time_vr0']:
                            field_instance = JulianDay()

                        elif last_field_name in ['velocity_semiamplitude_K',]:
                            field_instance = Velocity()

                        elif last_field_name in ['calculated_temperature', 'measured_temperature']:
                            field_instance = Temperature()

                        elif last_field_name in ['geometric_albedo',]:
                            field_instance = Albedo()

                        elif last_field_name in ['surface_gravity',]:
                            field_instance = Gravity()

                        if field_instance is not None and not math.isnan(value):
                            field_instance.value = value
                            field_instance.save()
                            setattr(exoplanet, field.name, field_instance)

                            if isinstance(field_instance, AstronomicalInfo):
                                last_field_info = field_instance


                else:
                    last_field_name = "this_impossible_field_name"

            if exoplanet.mass is not None and not math.isnan(exoplanet.mass.value):
                exoplanet.mass.unit = Mass.MASS_JUPITER
                exoplanet.mass.save()

            if exoplanet.radius is not None and not math.isnan(exoplanet.radius.value):
                exoplanet.radius.unit = Radius.RADIUS_JUPITER
                exoplanet.radius.save()

            exoplanet.save()
            return exoplanet

