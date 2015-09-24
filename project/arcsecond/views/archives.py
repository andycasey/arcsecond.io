from django.core import exceptions

from rest_framework import generics

from project.arcsecond import connectors
from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class ESOProgrammeSummaryDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.ESOProgrammeSummary.objects.all()
    serializer_class = serializers.ESOProgrammeSummarySerializer
    lookup_field = "programme_id"

    def get_object(self):
        programme_id = self.kwargs.get("programme_id", None)
        obj = connectors.get_ESO_programme_id_summary(programme_id)
        return obj


class ESOArchiveDataRowsListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ESOArchiveDataRow.objects.all().order_by("-date")
    serializer_class = serializers.ESOArchiveDataRowSerializer

    def get_queryset(self):
        # connectors.get_ESO_latest_data()
        return super(ESOArchiveDataRowsListAPIView, self).get_queryset().order_by("-date")



class HSTProgrammeSummaryDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.HSTProgrammeSummary.objects.all()
    serializer_class = serializers.HSTProgrammeSummarySerializer
    lookup_field = "programme_id"

    def get_object(self):
        programme_id = self.kwargs.get("programme_id", None)
        obj = connectors.get_STSCI_programme_id_summary("HST", programme_id)
        return obj

