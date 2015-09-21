
import json
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from django.shortcuts import render
from django.views.generic.edit import CreateView

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins
from project.arcsecond import forms
from project.arcsecond.views import get_generic_meta


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

class ObservingSiteActivityListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ObservingSiteActivity.objects.all().order_by('-date')
    serializer_class = serializers.ObservingSiteActivitySerializer

class ObservingSiteNamedDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"


def observingsites_map(request, path=None):
    context = {}
    context['angular_app'] = "arcsecondApp"
    context['api_root_url'] = settings.ARCSECOND_API_ROOT_URL
    context['meta'] = get_generic_meta(title="arcsecond.io", url=reverse_lazy('index_www'))
    return render(request, 'arcsecond/observingsites.html', context)


