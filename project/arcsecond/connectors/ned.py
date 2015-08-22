
import urllib2
from project.arcsecond.models import *
from astropy.io import votable
from django.core.exceptions import MultipleObjectsReturned

NED_ROOT_URL = "http://ned.ipac.caltech.edu/cgi-bin/objsearch?objname={0}&extend=yes&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=RA+or+Longitude&of=xml_all"

def get_NED_properties(name):
    url = NED_ROOT_URL.format(urllib2.quote(name))

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return None

    try:
        response_votable = votable.parse(response.fp)
    except:
        return None
    else:

        obj, created = AstronomicalObject.objects.get_with_aliases_or_create(name)




        return None