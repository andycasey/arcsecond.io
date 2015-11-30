from django.contrib import auth
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

class UserDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = auth.get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

class PublicationDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.Publication.objects.all()
    serializer_class = serializers.PublicationSerializer
    lookup_field = "bibcode"

    def get_object(self):
        bibcode = self.kwargs.get("bibcode", None)
        publication = connectors.get_ADS_publication_from_bibcode(bibcode)
        return publication

class PublicationListAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.Publication.objects.all()
    serializer_class = serializers.PublicationSerializer

    def get_queryset(self):
        query = self.kwargs.get("query", None)
        publications = connectors.get_ADS_publications_list_from_querystring(query)
        return publications
