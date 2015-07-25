from rest_framework import generics
from django.core import exceptions

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

        # try:
        #     obj = models.ESOProgrammeSummary.objects.get(programme_id=programme_id)
        # except exceptions.ObjectDoesNotExist:
        obj = connectors.get_ESO_programme_id_summary(programme_id)

        return obj