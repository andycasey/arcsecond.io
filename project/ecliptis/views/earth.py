from rest_framework import generics
from django.shortcuts import render

from project.iobserve import models
from project.iobserve import serializers

# Django doc: Note that this method returns a ValuesListQuerySet. This class behaves like a list.
# Most of the time this is enough, but if you require an actual Python list object, you can simply call list() on it,
#  which will evaluate the queryset
class SiteCoordinatesList(generics.ListCreateAPIView):
    queryset = models.ObservingSite.objects.all().values_list('coordinates', flat=True)
    serializer_class = serializers.CoordinatesSerializer

class SiteCoordinatesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ObservingSite.objects.all().values_list('coordinates', flat=True)
    serializer_class = serializers.CoordinatesSerializer

class ObservingSiteList(generics.ListCreateAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer

class ObservingSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer

def earth_browse(request, path=None):
    african_sites = models.ObservingSite.objects.filter(continent='Africa')
    antarctica_sites = models.ObservingSite.objects.filter(continent='Antarctica')
    asian_sites = models.ObservingSite.objects.filter(continent='Asia')
    european_sites = models.ObservingSite.objects.filter(continent='Europe')
    north_american_sites = models.ObservingSite.objects.filter(continent='North America')
    oceania_sites = models.ObservingSite.objects.filter(continent='Oceania')
    south_american_sites = models.ObservingSite.objects.filter(continent='South America')

    return render(request, 'iobserve/earth_browse.html', {'african_sites': african_sites,
                                                          'antarctica_sites': antarctica_sites,
                                                          'asian_sites': asian_sites,
                                                          'european_sites': european_sites,
                                                          'north_american_sites': north_american_sites,
                                                          'oceania_sites': oceania_sites,
                                                          'south_american_sites': south_american_sites})