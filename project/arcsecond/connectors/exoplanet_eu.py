import string
import urllib2
import timestring

from project.arcsecond.models import *
from astropy.io import votable
from django.core.exceptions import MultipleObjectsReturned

EXOPLANET_EU_URL = "http://exoplanet.eu/catalog/votable/"
EXOPLANET_EU_URL_FORMAT = "http://exoplanet.eu/catalog/votable/?f=%22{}%22+in+name"

def read_EXOPLANET_EU_full_catalog():
    try:
        response = urllib2.urlopen(EXOPLANET_EU_URL)
    except urllib2.URLError:
        return None

    try:
        response_votable = votable.parse(response.fp)
        first_table = response_votable.get_first_table()
    except:
        return None

    for row in xrange(len(first_table.array)):
        name = first_table.array[row][0]
        get_exoplanet(name, first_table.fields, first_table.array[row])


def get_EXOPLANET_EU_object(name):
    url = EXOPLANET_EU_URL_FORMAT.format(urllib2.quote(name))

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return None

    try:
        response_votable = votable.parse(response.fp)
        first_table = response_votable.get_first_table()
    except:
        return None

    exoplanet = get_exoplanet(name, first_table.fields, first_table.array[0])
    return exoplanet



def get_exoplanet(name, fields, values):
    try:
        exoplanet, created = Exoplanet.objects.get_or_create(name=name)
    except MultipleObjectsReturned:
        exoplanet = Exoplanet.objects.filter(name=name).first()

    for index, field in enumerate(fields):
        if field.name == 'star_name':
            try:
                value = values[index]
            except IndexError:
                pass
            else:
                parent_star, created = AstronomicalObject.objects.get_with_aliases_or_create(name=value)
                exoplanet.parent_star = parent_star
            break

    last_field_name = "this_impossible_field_name"
    last_field_info = None

    property_names = {'discovered': 'discovery_date',
                      'updated': 'last_update',
                      'tperi': 'time_periastron',
                      'tconj': 'time_conjonction',
                      'tzero_tr': 'primary_transit',
                      'tzero_tr_sec': 'secondary_transit',
                      'tzero_vr': 'time_radial_velocity_zero',
                      'k': 'velocity_semiamplitude',
                      'temp_calculated': 'calculated_temperature',
                      'temp_measured': 'measured_temperature',
                      'hot_point_lon': 'hottest_point_longitude',
                      'log_g': 'surface_gravity',
                      'detection_type': 'detection_method',
                      'mass_detection_type': 'mass_detection_method',
                      'radius_detection_type': 'radius_detection_method'}

    for index, field in enumerate(fields):
        if last_field_info is not None and field.name in [last_field_name+"_error_min", last_field_name+"_error_max"]:
            error_name = string.join(field.name.split("_")[-2:], "_")
            try:
                value = float(values[index])
            except ValueError:
                pass
            else:
                if not math.isnan(value):
                    setattr(last_field_info, error_name, value)
                    last_field_info.save()

        else:
            last_field_name = field.name
            last_field_info = None
            field_instance = None

            try:
                value = values[index]
            except IndexError:
                pass
            else:
                try:
                    float_value = float(value)
                except ValueError:
                    float_value = None
                else:
                    float_value = None if math.isnan(float_value) else float_value

                if last_field_name in ['ra', 'dec']:
                    if exoplanet.coordinates is None:
                        coordinates = AstronomicalCoordinates.get_or_create()
                        exoplanet.coordinates = coordinates

                    if float_value is not None:
                        attr_name = "right_ascension" if last_field_name == "ra" else "declination"
                        setattr(exoplanet.coordinates, attr_name, float_value)
                        setattr(exoplanet.coordinates, attr_name+"_units", "degrees")

                elif last_field_name in ['mag_b', 'mag_v', 'mag_r', 'mag_i', 'mag_j', 'mag_h', 'mag_k'] and float_value is not None:
                    flux_name = string.join([ sub.capitalize() for sub in last_field_name.split("_")], " ")
                    flux, created = Flux.objects.filter(astronomical_object=exoplanet.parent_star).get_or_create(name=flux_name)
                    flux.astronomical_object = exoplanet.parent_star
                    flux.value = float_value
                    flux.save()

                elif last_field_name == 'star_distance' and float_value is not None:
                    distance = Distance(value=float_value, unit=Distance.DISTANCE_PC)
                    distance.save()
                    exoplanet.parent_star.distance = distance

                elif last_field_name == 'star_teff' and float_value is not None:
                    temp = Temperature(value=float_value, unit=Temperature.TEMP_KELVIN)
                    temp.save()
                    exoplanet.parent_star.effective_temperature = temp

                elif last_field_name == 'star_mass' and float_value is not None:
                    mass = Mass(value=float_value, unit=Mass.MASS_SUN)
                    mass.save()
                    exoplanet.parent_star.mass = mass

                elif last_field_name == 'star_radius' and float_value is not None:
                    radius = Radius(value=float_value, unit=Radius.RADIUS_SUN)
                    radius.save()
                    exoplanet.parent_star.radius = radius

                elif last_field_name == 'star_metallicity' and float_value is not None:
                    metal = Metallicity(value=float_value)
                    metal.save()
                    exoplanet.parent_star.metallicity = metal

                elif last_field_name == 'star_age' and float_value is not None:
                    age = Age(value=float_value, unit=Age.AGE_GYR)
                    age.save()
                    exoplanet.parent_star.age = age

                elif last_field_name == 'star_sp_type':
                    exoplanet.parent_star.spectral_type = value

                # Missing: star_detected_disc, star_magnetic_field

                # elif last_field_name in ['discovered', 'updated']:
                #     try:
                #         date_value = timestring.Date(value)
                #     except:
                #         pass
                #     else:
                #         if date_value is not None:
                #             setattr(exoplanet, property_names.get(last_field_name, last_field_name), date_value)

                elif last_field_name in ['detection_type', 'mass_detection_type', 'radius_detection_type']:
                    string_value = Exoplanet.DETECTION_METHOD_UNKNOWN
                    if 'radial' in value.lower():
                        string_value = Exoplanet.DETECTION_METHOD_RV
                    elif 'lensing' in value.lower():
                        string_value = Exoplanet.DETECTION_METHOD_MICROLENSING
                    elif 'transit' in value.lower():
                        string_value = Exoplanet.DETECTION_METHOD_TRANSIT
                    elif 'timing' in value.lower():
                        string_value = Exoplanet.DETECTION_METHOD_TIMING
                    elif 'astrometry' in value.lower():
                        string_value = Exoplanet.DETECTION_METHOD_ASTROMETRY
                    elif 'imag' in value.lower():
                        string_value = Exoplanet.DETECTION_METHOD_IMAGING
                    setattr(exoplanet, last_field_name, string_value)

                elif last_field_name in ['inclination', 'omega_angle', 'anomaly_angle',  'lambda_angle', 'impact_parameter', 'hot_point_lon']:
                    field_instance = Angle(value=float_value, unit=Angle.ANGLE_DEGREE)

                elif last_field_name in ['semi_major_axis',]:
                    field_instance = EllipseAxis(value=float_value, unit=EllipseAxis.AXIS_UA)

                elif last_field_name in ['orbital_period',]:
                    field_instance = Period(value=float_value, unit=Period.PERIOD_DAY)

                elif last_field_name in ['eccentricity',]:
                    field_instance = Eccentricity(value=float_value)

                elif last_field_name in ['tperi', 'tconj', 'tzero_tr', 'tzero_tr_sec']:
                    field_instance = JulianDay(value=float_value)

                elif last_field_name in ['k',]:
                    field_instance = Velocity(value=float_value)

                elif last_field_name in ['temp_calculated', 'temp_measured']:
                    field_instance = Temperature(value=float_value, unit=Temperature.TEMP_KELVIN)

                elif last_field_name in ['geometric_albedo',]:
                    field_instance = Albedo(value=float_value)

                elif last_field_name in ['surface_gravity',]:
                    field_instance = Gravity(value=float_value)

                exoplanet.parent_star.save()

                if field_instance is not None:
                    if isinstance(field_instance, Mass):
                        field_instance.unit = Mass.MASS_JUPITER
                    elif isinstance(field_instance, Radius):
                        field_instance.unit = Radius.RADIUS_JUPITER

                    field_instance.save()
                    setattr(exoplanet, property_names.get(last_field_name, last_field_name), field_instance)

                    if isinstance(field_instance, AstronomicalInfo):
                        last_field_info = field_instance

    if exoplanet is not None:
        exoplanet.save()

    return exoplanet
