from rest_framework import generics

from project.arcsecond import connectors
from project.arcsecond import serializers
from project.arcsecond import models
from project.arcsecond import mixins

class PersonDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def get_object(self):
        name = self.kwargs.get("name", None)
        queryset = self.get_queryset().filter(last_name=name)
        person = generics.get_object_or_404(queryset)
        return person



class PublicationDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.Publication.objects.all()
    serializer_class = serializers.PublicationSerializer
    lookup_field = "bibcode"

    def get_object(self):
        bibcode = self.kwargs.get("bibcode", None)
        publication = connectors.get_ADS_publication(bibcode=bibcode)
        return publication

