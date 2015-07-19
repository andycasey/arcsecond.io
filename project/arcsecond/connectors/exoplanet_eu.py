import string
import urllib2
from rest_framework import status
from project.arcsecond.models import *
from astropy.io import votable
from django.core.exceptions import MultipleObjectsReturned

EXOPLANET_EU_URL_FORMAT = "http://exoplanet.eu/catalog/votable/?f=%22{}%22+in+name"

def get_EXOPLANET_EU_object(name):
    url = EXOPLANET_EU_URL_FORMAT.format(urllib2.quote(name))

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return None, Messages(error="Invalid URL", http_status_code=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            response_votable = votable.parse(response.fp)
            first_table = response_votable.get_first_table()
        except:
            return None, Messages(error="Unrecognized identifier or invalid VO Table for exoplanet", http_status_code=status.HTTP_204_NO_CONTENT)
        else:
            name = first_table.array[0][0]

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
                        value = float(first_table.array[0][index])
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
                                value = float(first_table.array[0][index])
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

            return exoplanet, Messages(http_status_code=200)

