from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

import views
import api

urlpatterns = patterns('',
  url(r'^sky/object/(?P<name>[0-9a-zA-Z_-]+)/?$', views.astronomical_object),
  url(r'^sky/object/(?P<name>[0-9a-zA-Z_-]+)/coordinates/?$', views.astronomical_coordinates, name='coordinates-detail'),
  url(r'^sky/object/(?P<name>[0-9a-zA-Z_-]+)/aliases/?$', views.astronomical_object_aliases, name='alias-list'),
  # url(r'^sky/object/(?P<name>[0-9a-zA-Z_-]+)/references/$', api.BibliographicReferenceList.as_view(), name='references-list'),
  # url(r'^sky/object/(?P<name>[0-9a-zA-Z_-]+)/reference/(?P<bibcode>[0-9a-zA-Z_-]+)/authors$', api.AliasList.as_view(), name='authors-list'),
  # url(r'^sky/object/(?P<name>[0-9a-zA-Z_-]+)/infos/$', api.AliasList.as_view(), name='infos-list'),
)

urlpatterns += format_suffix_patterns(urlpatterns)
