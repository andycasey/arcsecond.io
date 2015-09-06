
from rest_framework import generics
from django.shortcuts import render

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class TelescopeListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.Telescope.objects.all()
    serializer_class = serializers.TelescopeSerializer
    lookup_field = "name"

    def get_queryset(self):
        queryset = models.Telescope.objects.all()
        continent = self.request.query_params.get('continent', None)
        if continent is not None:
            queryset = queryset.filter(observing_site__continent=continent)
        return queryset


class TelescopeDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.Telescope.objects.all()
    serializer_class = serializers.TelescopeSerializer
    lookup_field = "name"

    # def get_object(self):
    #     name = self.kwargs.get("name", None)
    #     return self.get_queryset().get(name=name)


def telescopes(request, path=None):
    african_telescopes = models.Telescope.objects.filter(observing_site__continent='Africa')
    antarctica_telescopes = models.Telescope.objects.filter(observing_site__continent='Antarctica')
    asian_telescopes = models.Telescope.objects.filter(observing_site__continent='Asia')
    european_telescopes = models.Telescope.objects.filter(observing_site__continent='Europe')
    north_american_telescopes = models.Telescope.objects.filter(observing_site__continent='North America')
    oceania_telescopes = models.Telescope.objects.filter(observing_site__continent='Oceania')
    south_american_telescopes = models.Telescope.objects.filter(observing_site__continent='South America')

    return render(request, 'webapp/telescopes.html', {'african_telescopes': african_telescopes.count,
                                                      'antarctica_telescopes': antarctica_telescopes.count,
                                                      'asian_telescopes': asian_telescopes.count,
                                                      'european_telescopes': european_telescopes.count,
                                                      'north_american_telescopes': north_american_telescopes.count,
                                                      'oceania_telescopes': oceania_telescopes.count,
                                                      'south_american_telescopes': south_american_telescopes.count})


