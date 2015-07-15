import urllib2
from rest_framework import status
from ..models import *

EXOPLANET_EU_URL_FORMAT = "http://exoplanet.eu/catalog/votable/?f=%%22{}%%22+in+name"

def get_EXOPLANET_EU_object(name):
    url = EXOPLANET_EU_URL_FORMAT.format(name)

    try:
        response = urllib2.urlopen(urllib2.quote(url))
    except urllib2.URLError:
        return None, Messages(error="Invalid URL", http_status_code=status.HTTP_400_BAD_REQUEST)
    else:
        pass

