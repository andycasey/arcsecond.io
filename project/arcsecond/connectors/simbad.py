
import urllib2
from project.arcsecond.models import *
from astropy.io import votable
from django.core.exceptions import MultipleObjectsReturned

SIMBAD_VOTABLE_SCRIPT_START   = "votable v1 {\n"
SIMBAD_VOTABLE_SCRIPT_MIDDLE  = "}\nvotable open v1\n"
SIMBAD_VOTABLE_SCRIPT_END     = "\nvotable close"
SIMBAD_BASIC_SCRIPT		      = "format object "

QUERY_VOTABLE_FULLCOORDINATES = "COO(d;ICRS;2000;2000)\n"
QUERY_VOTABLE_PROPERMOTION    = "PROPERMOTIONS\n"
QUERY_VOTABLE_PARALLAX        = "PARALLAX\n"
QUERY_VOTABLE_VELOCITY        = "VELOCITY\n"
QUERY_VOTABLE_SPECTRALTYPE    = "SPTYPE\n"
QUERY_VOTABLE_MORPHOTYPE      = "MORPHTYPE\n"
QUERY_VOTABLE_ALIASES         = "IDLIST\n"
QUERY_VOTABLE_TYPES           = "OTYPELIST(V)\n"
QUERY_VOTABLE_FLUXES          = "FLUXDATA(U)\nFLUXDATA(B)\nFLUXDATA(V)\nFLUXDATA(R)\nFLUXDATA(I)\nFLUXDATA(J)\nFLUXDATA(H)\nFLUXDATA(K)\nFLUXDATA(B)\nFLUXDATA(u)\nFLUXDATA(g)\nFLUXDATA(r)\nFLUXDATA(i)\nFLUXDATA(z)\n"

VOTABLE_OPTIONS   = "output console=off script=off\n"
NAME_SCRIPT       = "sim-script?script="
QUERY_ALIAS       = '"%IDLIST"\n'
QUERY_FLUX        = '"$%FLUXLIST[%%*(N=F )]"\n'
QUERY_COORDS      = '"$%COO($A$D)"\n'
QUERY_OTYPE       = '"$%OTYPE(S)"\n'
QUERY_OTYPELONG   = '"$%OTYPE(V)"\n'
QUERY_OTYPES      = '"$%OTYPELIST(V,)"\n'
QUERY_BIBNUMBER   = '"$%23BIBCODELIST"\n'
QUERY_REFERENCE   = '"$%REFLIST($%B$%1A,)"\n'

QUERY_ERROR_DELIMITER  = "::error::"
QUERY_DATA_DELIMITER   = "::data::"
COORDS_NO_OBJECTS      = "!! No astronomical object found"

SIMBAD_ROOT_1 = "http://simbad.harvard.edu/simbad/"
SIMBAD_ROOT_2 = "http://simbad.u-strasbg.fr/simbad/"
VIZIER_OBJECT_URL_ROOT = "http://vizier.u-strasbg.fr/viz-bin/VizieR-S"

def get_SIMBAD_coordinates(name):
    url = VOTABLE_OPTIONS + SIMBAD_VOTABLE_SCRIPT_START + QUERY_VOTABLE_FULLCOORDINATES + SIMBAD_VOTABLE_SCRIPT_MIDDLE + name + SIMBAD_VOTABLE_SCRIPT_END

    try:
        response = urllib2.urlopen(SIMBAD_ROOT_1+NAME_SCRIPT+urllib2.quote(url))
    except urllib2.URLError:
        try:
            response = urllib2.urlopen(SIMBAD_ROOT_2+NAME_SCRIPT+urllib2.quote(url))
        except urllib2.URLError:
            return None

    try:
        response_votable = votable.parse(response.fp)
        first_table = response_votable.get_first_table()
    except:
        return None
    else:
        ra = float(first_table.array[0][0])
        dec = float(first_table.array[0][1])

        try:
            coords, created = AstronomicalCoordinates.objects.get_or_create(right_ascension=ra, declination=dec)
        except MultipleObjectsReturned:
            coords = AstronomicalCoordinates.objects.filter(right_ascension=ra, declination=dec).first()

        return coords


def get_SIMBAD_aliases(name):
    url = SIMBAD_BASIC_SCRIPT + QUERY_ALIAS + name

    try:
        response = urllib2.urlopen(SIMBAD_ROOT_1+NAME_SCRIPT+urllib2.quote(url))
    except urllib2.URLError:
        try:
            response = urllib2.urlopen(SIMBAD_ROOT_2+NAME_SCRIPT+urllib2.quote(url))
        except urllib2.URLError:
            return None

    aliases = []
    ok = False

    for line in response.readlines():
        if ok and len(line.strip()) > 0:
            alias, created = Alias.objects.get_or_create(name=line.strip())
            alias.catalogue_url = VIZIER_OBJECT_URL_ROOT + "?" + urllib2.quote(alias.name.encode('utf8'))
            aliases.append(alias)
        if line.find(QUERY_DATA_DELIMITER) >= 0:
            ok = True

    return aliases


def get_SIMBAD_object_types(name):
    url = SIMBAD_BASIC_SCRIPT + QUERY_OTYPES + name

    try:
        response = urllib2.urlopen(SIMBAD_ROOT_1+NAME_SCRIPT+urllib2.quote(url))
    except urllib2.URLError:
        try:
            response = urllib2.urlopen(SIMBAD_ROOT_2+NAME_SCRIPT+urllib2.quote(url))
        except urllib2.URLError:
            return None

    otypes = []
    ok = False

    value_line = None
    for line in response.readlines():
        if ok and len(line.strip()) > 0:
            value_line = line.strip()
        if line.find(QUERY_DATA_DELIMITER) >= 0:
            ok = True

    if len(value_line) > 0:
        values = value_line.split(",")
        for value in values:
            otype, created = ObjectType.objects.get_or_create(value=value)
            otypes.append(otype)

    return otypes


def get_SIMBAD_fluxes(name):
    url = VOTABLE_OPTIONS + SIMBAD_VOTABLE_SCRIPT_START + QUERY_VOTABLE_FLUXES + SIMBAD_VOTABLE_SCRIPT_MIDDLE + name + SIMBAD_VOTABLE_SCRIPT_END

    try:
        response = urllib2.urlopen(SIMBAD_ROOT_1+NAME_SCRIPT+urllib2.quote(url))
    except urllib2.URLError:
        try:
            response = urllib2.urlopen(SIMBAD_ROOT_2+NAME_SCRIPT+urllib2.quote(url))
        except urllib2.URLError:
            return None

    response_votable = votable.parse(response)
    first_table = response_votable.get_first_table()

    filters = ["U", "B", "V", "R", "I", "J", "H", "K", "u", "g", "r", "i", "z"]
    fluxes = []

    for filter in filters:
        filter_name = first_table.array["FILTER_NAME_"+filter]
        flux_value = first_table.array["FLUX_"+filter]

        if len(filter_name) == 1 and len(flux_value) == 1 and len(filter_name[0]) > 0 and not math.isnan(flux_value[0]):
            flux = Flux(name=filter_name[0], value=flux_value[0])

            flux_error_value = first_table.array["FLUX_ERROR_"+filter]
            if len(flux_error_value) == 1 and not math.isnan(flux_error_value[0]):
                flux.error_value = flux_error_value[0]

            flux_bibcode = first_table.array["FLUX_BIBCODE_"+filter]
            if len(flux_bibcode) == 1 and len(flux_bibcode[0]) > 0:
                flux.bibcode = flux_bibcode[0]

            flux_unit = first_table.array["FLUX_UNIT_"+filter]
            if len(flux_unit) == 1 and len(flux_unit[0]) > 0:
                flux.unit = flux_unit[0]

            fluxes.append(flux)

    return fluxes

