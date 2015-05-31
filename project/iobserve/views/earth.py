from rest_framework import generics
from django.shortcuts import render

from ..serializers import *
from ..simbad import *


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