
from rest_framework import generics
from rest_framework import permissions

from .models import *
from .serializers import *

class AstronomicalObjectDetail(generics.RetrieveAPIView):
  model = AstronomicalObject
  serializer_class = AstronomicalObjectSerializer

class AliasDetail(generics.RetrieveAPIView):
  model = Alias
  serializer_class = AliasSerializer

class AliasList(generics.ListCreateAPIView):
  model = Alias
  serializer_class = AliasSerializer

class BibliographicReferenceList(generics.ListCreateAPIView):
  model = BibliographicReference
  serializer_class = BibliographicReferenceSerializer

class AuthorList(generics.ListCreateAPIView):
  model = Person
  serializer_class = PersonSerializer

