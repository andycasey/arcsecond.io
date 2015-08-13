
from rest_framework import generics

from project.arcsecond import connectors
from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class AstronomersTelegramDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.AstronomersTelegram.objects.all()
    serializer_class = serializers.AstronomersTelegramSerializer
    lookup_field = "identifier"

    def get_object(self):
        identifier = self.kwargs.get("identifier", None)
        telegram = connectors.get_ATel(identifier=identifier)
        return telegram

