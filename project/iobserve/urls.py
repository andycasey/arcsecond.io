from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

import views

urlpatterns = patterns('',
  # url(r'^$', views.index, name='index'),
  # url(r'^index', views.index, name='index'),
  # url(r'^about', views.about, name='about'),
  # url(r'^sky/object/?$', views.astronomical_object),
  url(r'^sky/object/(?P<name>[0-9a-zA-Z_-]+)/?$', views.astronomical_object),
)

urlpatterns += format_suffix_patterns(urlpatterns)
