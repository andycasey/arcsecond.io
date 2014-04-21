
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

import urllib2
from astropy.io import votable

SIMBAD_ROOT = "http://simbad.harvard.edu/simbad/sim-script?script="
coords_script = "output console=off script=off\nvotable v1 {\nCOO(d;ICRS;2000;2000)\n}\nvotable open v1\n%s\nvotable close"

@api_view(['GET'])
def astronomical_object(request, name="."):
  coords_url = SIMBAD_ROOT+urllib2.quote(coords_script%name)

  try:
    response = urllib2.urlopen(coords_url)
  except urllib2.URLError:
    return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
  else:
    response_votable = votable.parse(response)
    coords_table = response_votable.get_first_table()
      
    coords = AstronomicalCoordinates(source="SIMBAD")
    coords.right_ascension = float(coords_table.array[0][0])
    coords.declination = float(coords_table.array[0][1])
    coords.save()
            
    obj = AstronomicalObject(name=name, coordinates=coords)
    obj.save()
        
    serializer = AstronomicalObjectSerializer(obj)
    return Response(serializer.data)
  
  
