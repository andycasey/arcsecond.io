from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response, render

from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model

from rest_framework import generics

from project.arcsecond import connectors
from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

# from .. import forms

class UserProfileListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

class UserProfileDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

class UserProfileNamedDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs.get("username", None)
        queryset = self.get_queryset().filter(user__username=username)
        profile = generics.get_object_or_404(queryset)
        return profile
