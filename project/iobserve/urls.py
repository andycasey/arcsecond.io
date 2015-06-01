from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns
from django.conf.urls import url

import views
import api

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),

    url(r'^accounts/profile/?$', views.UserProfileView, name='user-profile'),

    url(r'^sky/?$', views.sky_home),

    url(r'^sky/1/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/?$', views.astronomical_object, name='sky-object'),
    url(r'^sky/1/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/coordinates/?$', views.astronomical_coordinates, name='sky-object-coordinates'),
    url(r'^sky/1/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/aliases/?$', views.astronomical_object_aliases, name='sky-object-aliases'),

    # url(r'^sky/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/?$', RedirectView.as_view(url=reverse('sky-object'), permanent=True)),

    url(r'^earth/?$', views.earth_home, name="earth-home"),
    url(r'^earth/browse/?$', views.earth_browse, name="earth-browse"),

    url(r'^earth/site/?$', views.ObservingSiteList.as_view(), name='site-list'),
    url(r'^earth/site/(?P<pk>[0-9]+)/?$', views.ObservingSiteDetail.as_view(), name='site-list'),

    url(r'^earth/site/coordinates/?$', views.SiteCoordinatesList.as_view(), name='terrestrialcoordinates-list'),
    url(r'^earth/site/coordinates/(?P<pk>[0-9]+)/?$', views.SiteCoordinatesDetail.as_view(), name='terrestrialcoordinates-detail'),
)

urlpatterns += format_suffix_patterns(urlpatterns)



