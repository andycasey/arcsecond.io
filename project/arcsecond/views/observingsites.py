
from rest_framework import generics
from django.shortcuts import render
from django.views.generic.edit import CreateView

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins
from project.arcsecond import forms

class ObservingSiteListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"

    def get_queryset(self):
        queryset = models.ObservingSite.objects.all()
        continent = self.request.query_params.get('continent', None)
        if continent is not None:
            queryset = queryset.filter(continent=continent)
        return queryset


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


class ObservingSiteCreateView(CreateView):
    model = models.ObservingSite
    template_name = 'webapp/new_observingsite.html'
    form_class = forms.ObservingSiteForm
    context_object_name = "context"
