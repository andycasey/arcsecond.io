
from rest_framework import generics

from project.arcsecond import connectors
from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class FindingChartDetailAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.FindingChart.objects.all()
    serializer_class = serializers.FindingChartSerializer

    def get(self, request, *args, **kwargs):
        input_value = self.kwargs.get("input_value", None)
        charts = connectors.get_OPTIR_charts(input=input_value)
        return super(FindingChartDetailAPIView, self).get(request, *args, **kwargs)
