from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

import views
import api

urlpatterns = patterns('',
    url(r'^sky/1/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/?$', views.astronomical_object),
    url(r'^sky/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/?$', views.astronomical_object),
    url(r'^sky/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/coordinates/?$', views.astronomical_coordinates, name='coordinates-detail'),
    url(r'^sky/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/aliases/?$', views.astronomical_object_aliases, name='alias-list'),

    url(r'^sky/?$', views.sky_home),
    url(r'^sky/(?P<path>[\s\+0-9a-zA-Z_-]+)/?$', views.sky_home),

    url(r'^earth/site/coordinates/all/?$', views.TerrestrialCoordinatesList.as_view(), name='terrestrialcoordinates-list'),
    url(r'^earth/site/coordinates/(?P<pk>[0-9]+)/?$', views.TerrestrialCoordinatesDetail.as_view(), name='terrestrialcoordinates-detail'),

    url(r'^earth/site/all/?$', views.SiteList.as_view(), name='site-list'),
    url(r'^earth/observing_site/all/?$', views.ObservingSiteList.as_view(), name='observingsite-list'),

    url(r'^earth/?$', views.earth_home),
    url(r'^earth/(?P<path>[\s\+0-9a-zA-Z_-]+)/?$', views.earth_home),
)

urlpatterns += format_suffix_patterns(urlpatterns)


