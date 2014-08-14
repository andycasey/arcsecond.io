from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render, render_to_response

from .models import *
from .serializers import *

from simbad import *

@api_view(['GET'])
def astronomical_object(request, name="."):
    obj, created = AstronomicalObject.objects.get_or_create(name=name)

    if created:
        coords = get_SIMBAD_coordinates(name)

        if coords is None:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        obj.coordinates = coords
        obj.save()

        aliases = get_SIMBAD_aliases(name)

        if aliases is None:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        obj.aliases = aliases
        obj.save()

    serializer = AstronomicalObjectSerializer(obj)
    return Response(serializer.data)


@api_view(['GET'])
def astronomical_coordinates(request, name="."):
    coords = get_SIMBAD_coordinates(name)

    if coords is None:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    serializer = AstronomicalCoordinatesSerializer(coords)
    return Response(serializer.data)


@api_view(['GET'])
def astronomical_object_aliases(request, name="."):
    aliases = get_SIMBAD_aliases(name)

    if aliases is None:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    serializer = AliasSerializer(aliases, many=True)
    return Response(serializer.data)


class TerrestrialCoordinatesList(generics.ListCreateAPIView):
    queryset = TerrestrialCoordinates.objects.all()
    serializer_class = TerrestrialCoordinatesSerializer


class TerrestrialCoordinatesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TerrestrialCoordinates.objects.all()
    serializer_class = TerrestrialCoordinatesSerializer


class SiteList(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ObservingSiteList(generics.ListCreateAPIView):
    queryset = ObservingSite.objects.all()
    serializer_class = ObservingSiteSerializer


class ObservingSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObservingSite.objects.all()
    serializer_class = ObservingSiteSerializer



    # @api_view(['GET'])
    # def terrestrial_coordinates(request, pk):
    # coords = TerrestrialCoordinates.get(pk=pk)
    #
    # if coords == None:
    # return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    #
    #   serializer = TerrestrialCoordinatesSerializer(coords)
    #   return Response(serializer.data)
    #
    #
    # @api_view(['GET'])
    # def terrestrial_coordinates_all(request):
    #   coords = TerrestrialCoordinates.objects.all()
    #
    #   if coords == None:
    #     return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    #
    #   serializer = TerrestrialCoordinatesSerializer(coords, many=True)
    #   return Response(serializer.data)
    #
    #
    #


def custom_404(request):
    return render(request, 'iobserve/404.html')

def sky_home(request, path=None):
    return render(request, 'iobserve/sky_home.html', {'api_version': '1'})

def earth_home(request, path=None):
    return render(request, 'iobserve/earth_home.html', {'api_version': '1'})
