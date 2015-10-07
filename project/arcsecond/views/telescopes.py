
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


class TelescopeNamedDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.Telescope.objects.all()
    serializer_class = serializers.TelescopeSerializer
    lookup_field = 'name'

