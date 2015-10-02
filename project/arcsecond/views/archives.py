from django.core import exceptions

import timestring
import datetime

from rest_framework import generics
from rest_framework import pagination

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


class ESOArchiveDataRowsListPagination(pagination.PageNumberPagination):
    page_size = 1000

class ESOArchiveDataRowsListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ESOArchiveDataRow.objects.all().order_by("-date")
    serializer_class = serializers.ESOArchiveDataRowSerializer
    pagination_class = ESOArchiveDataRowsListPagination

    def get_queryset(self):
        params = self.request.query_params
        date_start_string = params.get("start", None)
        connectors.get_ESO_latest_data(start_date=date_start_string)

        qs = super(ESOArchiveDataRowsListAPIView, self).get_queryset().order_by("-date")

        if date_start_string is not None:
            date_no_microseconds = timestring.Date(date_start_string, tz="UTC").date
            if date_no_microseconds is not None:
                microseconds_string = date_start_string.split('.')[-1]
                microseconds = int(microseconds_string[:-1])*1000 + 500 # Avoid last Z letter
                date_start = date_no_microseconds + datetime.timedelta(microseconds=microseconds)
                qs = qs.filter(date__gt=date_start)

        return qs


class HSTProgrammeSummaryDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.HSTProgrammeSummary.objects.all()
    serializer_class = serializers.HSTProgrammeSummarySerializer
    lookup_field = "programme_id"

    def get_object(self):
        programme_id = self.kwargs.get("programme_id", None)
        obj = connectors.get_STSCI_programme_id_summary("HST", programme_id)
        return obj

