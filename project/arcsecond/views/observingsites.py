
from rest_framework import generics

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

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


