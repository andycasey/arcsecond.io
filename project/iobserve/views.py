
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

from simbad import *

@api_view(['GET'])
def astronomical_object(request, name="."):
  obj, created = AstronomicalObject.objects.get_or_create(name=name)
  
  if created:
    coords = get_SIMBAD_coordinates(name)
    
    if coords == None:
      return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
      
    obj.coordinates = coords;
    obj.save()
        
  # alias = Alias(name="toto")
  # alias.save()
        
  # obj.aliases = [alias,]
        
  serializer = AstronomicalObjectSerializer(obj)
  return Response(serializer.data)
    
    
@api_view(['GET'])
def astronomical_coordinates(request, name="."):
  coords = get_SIMBAD_coordinates(name)
  
  if coords == None:
    return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

  serializer = AstronomicalCoordinatesSerializer(coords)
  return Response(serializer.data)


@api_view(['GET'])
def astronomical_object_aliases(request, name="."):
  aliases = get_SIMBAD_aliases(name)

  if aliases == None:
    return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

  serializer = AliasSerializer(aliases, many=True)
  return Response(serializer.data)

