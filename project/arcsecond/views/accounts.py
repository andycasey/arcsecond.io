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


class UserListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

