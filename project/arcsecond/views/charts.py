
from rest_framework import generics

from project.arcsecond import connectors
from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class FindingChartDetailAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.FindingChart.objects.all()
    serializer_class = serializers.FindingChartSerializer

    def get_queryset(self):
        input_value = self.kwargs.get("input_value", None)
        chart_pks = connectors.get_OPTIR_charts(input=input_value)
        queryset = models.FindingChart.objects.filter(pk__in=chart_pks)
        return queryset
