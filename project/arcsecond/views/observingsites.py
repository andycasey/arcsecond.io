from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class ObservingSiteListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ObservingSite.objects.all().order_by('name')
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"

    def get_queryset(self):
        queryset = models.ObservingSite.objects.all().order_by('name')
        continent = self.request.query_params.get('continent', None)
        if continent is not None:
            queryset = queryset.filter(continent=continent)
        return queryset

class ObservingSiteActivityListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ObservingSiteActivity.objects.all().order_by('-date')
    serializer_class = serializers.ObservingSiteActivitySerializer

class ObservingSiteDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer

class ObservingSiteNamedDetailAPIView(ObservingSiteDetailAPIView):
    lookup_field = "name"

    def get_object(self):
        name = self.kwargs.get("name", None)
        queryset = self.get_queryset()

        try:
            obj = queryset.get(name=name)
        except ObjectDoesNotExist:
            try:
                obj = queryset.get(short_name=name)
            except ObjectDoesNotExist:
                try:
                    obj = queryset.get(alternate_name_1=name)
                except ObjectDoesNotExist:
                    try:
                        obj = queryset.get(alternate_name_2=name)
                    except ObjectDoesNotExist:
                        raise Http404()

        return obj


