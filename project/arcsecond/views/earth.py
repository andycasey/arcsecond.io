from rest_framework import generics
from django.shortcuts import render

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class CoordinatesDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.ObservingSite.objects.all().values_list('coordinates', flat=True)
    serializer_class = serializers.CoordinatesSerializer

class ObservingSiteListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"

class ObservingSiteDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"

def observingsites(request, path=None):
    african_sites = models.ObservingSite.objects.filter(continent='Africa')
    antarctica_sites = models.ObservingSite.objects.filter(continent='Antarctica')
    asian_sites = models.ObservingSite.objects.filter(continent='Asia')
    european_sites = models.ObservingSite.objects.filter(continent='Europe')
    north_american_sites = models.ObservingSite.objects.filter(continent='North America')
    oceania_sites = models.ObservingSite.objects.filter(continent='Oceania')
    south_american_sites = models.ObservingSite.objects.filter(continent='South America')

    return render(request, 'arcsecond/observingsites.html', {'african_sites': african_sites.count,
                                                              'antarctica_sites': antarctica_sites.count,
                                                              'asian_sites': asian_sites.count,
                                                              'european_sites': european_sites.count,
                                                              'north_american_sites': north_american_sites.count,
                                                              'oceania_sites': oceania_sites.count,
                                                              'south_american_sites': south_american_sites.count})