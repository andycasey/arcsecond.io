from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .serializers import *

from simbad import *

def index(request):
  context = RequestContext(request)
  context_dict = {"title": ("eclipt.is")}
  return render_to_response('iobserve/index.html', context_dict, context)


@api_view(['GET'])
def astronomical_object(request, name="."):
    obj, created = AstronomicalObject.objects.get_or_create(name=name)

    if created or obj.coordinates is None:
        coords = get_SIMBAD_coordinates(name)

        if coords is None:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        obj.coordinates = coords
        obj.save()

    if created or obj.aliases.all().count() == 0:
        aliases = get_SIMBAD_aliases(name)
        if len(aliases) > 0:
            obj.aliases = aliases
            obj.save()

    if created or obj.object_types.all().count() == 0:
        otypes = get_SIMBAD_object_types(name)
        if len(otypes) > 0:
            obj.object_types = otypes
            obj.save()

    if created or obj.fluxes.all().count() == 0 or len([f for f in obj.fluxes.all() if not f.is_valid()]) > 0:
        fluxes = get_SIMBAD_fluxes(name)
        if len(fluxes) > 0:
            obj.fluxes = fluxes
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


# Django doc: Note that this method returns a ValuesListQuerySet. This class behaves like a list.
# Most of the time this is enough, but if you require an actual Python list object, you can simply call list() on it,
#  which will evaluate the queryset
class SiteCoordinatesList(generics.ListCreateAPIView):
    queryset = ObservingSite.objects.all().values_list('coordinates', flat=True)
    serializer_class = CoordinatesSerializer

class SiteCoordinatesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObservingSite.objects.all().values_list('coordinates', flat=True)
    serializer_class = CoordinatesSerializer

class ObservingSiteList(generics.ListCreateAPIView):
    queryset = ObservingSite.objects.all()
    serializer_class = ObservingSiteSerializer


class ObservingSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObservingSite.objects.all()
    serializer_class = ObservingSiteSerializer



    # @api_view(['GET'])
    # def terrestrial_coordinates(request, pk):
    # coords = Coordinates.get(pk=pk)
    #
    # if coords == None:
    # return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    #
    #   serializer = EarthLocationSerializer(coords)
    #   return Response(serializer.data)
    #
    #
    # @api_view(['GET'])
    # def terrestrial_coordinates_all(request):
    #   coords = Coordinates.objects.all()
    #
    #   if coords == None:
    #     return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
    #
    #   serializer = EarthLocationSerializer(coords, many=True)
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

def earth_browse(request, path=None):
    african_sites = ObservingSite.objects.filter(continent='Africa')
    antarctica_sites = ObservingSite.objects.filter(continent='Antarctica')
    asian_sites = ObservingSite.objects.filter(continent='Asia')
    european_sites = ObservingSite.objects.filter(continent='Europe')
    north_american_sites = ObservingSite.objects.filter(continent='North America')
    oceania_sites = ObservingSite.objects.filter(continent='Oceania')
    south_american_sites = ObservingSite.objects.filter(continent='South America')

    return render(request, 'iobserve/earth_browse.html', {'african_sites': african_sites,
                                                          'antarctica_sites': antarctica_sites,
                                                          'asian_sites': asian_sites,
                                                          'european_sites': european_sites,
                                                          'north_american_sites': north_american_sites,
                                                          'oceania_sites': oceania_sites,
                                                          'south_american_sites': south_american_sites})
