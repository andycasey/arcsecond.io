
import urllib2
from .models import *
from astropy.io import votable
from django.core.exceptions import MultipleObjectsReturned

SIMBAD_VOTABLE_SCRIPT_START   = "votable v1 {\n"
SIMBAD_VOTABLE_SCRIPT_MIDDLE  = "}\nvotable open v1\n"
SIMBAD_VOTABLE_SCRIPT_END     = "\nvotable close"
SIMBAD_BASIC_SCRIPT				     = "format object "

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

SIMBAD_ROOT = "http://simbad.harvard.edu/simbad/"

def get_SIMBAD_coordinates(name):
  coords_url = VOTABLE_OPTIONS + SIMBAD_VOTABLE_SCRIPT_START + QUERY_VOTABLE_FULLCOORDINATES + \
              SIMBAD_VOTABLE_SCRIPT_MIDDLE + name + SIMBAD_VOTABLE_SCRIPT_END

  try:
    response = urllib2.urlopen(SIMBAD_ROOT+NAME_SCRIPT+urllib2.quote(coords_url))
  except urllib2.URLError:
    return None
  else:
    response_votable = votable.parse(response)
    coords_table = response_votable.get_first_table()

    ra = float(coords_table.array[0][0])
    dec = float(coords_table.array[0][1])

    try:
      coords, created = AstronomicalCoordinates.objects.get_or_create(right_ascension=ra, declination=dec)
    except MultipleObjectsReturned:
      coords = AstronomicalCoordinates.objects.filter(right_ascension=ra, declination=dec).first()
      
    return coords;



def get_SIMBAD_aliases(name):
  aliases_url = SIMBAD_BASIC_SCRIPT + QUERY_ALIAS + name
  print SIMBAD_ROOT+NAME_SCRIPT+urllib2.quote(aliases_url)

  try:
    response = urllib2.urlopen(SIMBAD_ROOT+NAME_SCRIPT+urllib2.quote(aliases_url))
  except urllib2.URLError:
    return None
  else:
    aliases = []
    ok = False
    
    for line in response.readlines():
      if ok and len(line.strip()) > 0:
        alias, created = Alias.objects.get_or_create(name=line.strip())
        aliases.append(alias)
      if line.find(QUERY_DATA_DELIMITER) >= 0:
        ok = True

    print aliases
    return aliases;




