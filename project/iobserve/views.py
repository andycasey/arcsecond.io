
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AstronomicalObject, AstronomicalCoordinates
from .serializers import AstronomicalObjectSerializer

import urllib2
from astropy.io import votable

root = "http://simbad.harvard.edu/simbad/sim-script?script="
parameters = "output console=off script=off\nvotable v1 {\nCOO(d;ICRS;2000;2000)\n}\nvotable open v1\n%s\nvotable close"

@api_view(['GET'])
def astronomical_object(request, name="."):
  url = root+urllib2.quote(parameters%name)
  
  response = urllib2.urlopen(url)
  response_votable = votable.parse(response)
  coords_table = response_votable.get_first_table()
    
  coords = AstronomicalCoordinates()
  coords.right_ascension = float(coords_table.array[0][0])
  coords.declination = float(coords_table.array[0][1])
  
  obj = AstronomicalObject()
  obj.name = "M2"
  obj.coordinates = coords
  
  serializer = AstronomicalObjectSerializer(obj)
  return Response(serializer.data)


