
from rest_framework import generics
from rest_framework import pagination

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


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AstronomersTelegramListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.AstronomersTelegram.objects.all().order_by('-identifier')
    serializer_class = serializers.AstronomersTelegramSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = "identifier"

    def get_queryset(self):
        connectors.read_last_ATels(StandardResultsSetPagination.page_size)
        return super(AstronomersTelegramListAPIView, self).get_queryset()