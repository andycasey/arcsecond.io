from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

import views
import api

# we subclass the view to redirect to home page after registration
# http://django-registration.readthedocs.org/en/latest/views.html#registration.views.RegistrationView.get_success_url
from registration.backends.simple.views import RegistrationView as SimpleRegistrationView
class RegistrationView(SimpleRegistrationView):
    def get_success_url(self, request, user):
        return ('/index.html', (), {})

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^sky/1/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/?$', views.astronomical_object),
    url(r'^sky/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/?$', views.astronomical_object),
    url(r'^sky/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/coordinates/?$', views.astronomical_coordinates, name='coordinates-detail'),
    url(r'^sky/object/(?P<name>[\s\+0-9a-zA-Z_-]+)/aliases/?$', views.astronomical_object_aliases, name='alias-list'),

    url(r'^sky/?$', views.sky_home),
    url(r'^sky/(?P<path>[\s\+0-9a-zA-Z_-]+)/?$', views.sky_home),

    url(r'^earth/site/coordinates/all/?$', views.EarthLocationList.as_view(), name='terrestrialcoordinates-list'),
    url(r'^earth/site/coordinates/(?P<pk>[0-9]+)/?$', views.EarthLocationDetail.as_view(), name='terrestrialcoordinates-detail'),

    url(r'^earth/site/all/?$', views.SiteList.as_view(), name='site-list'),
    url(r'^earth/observing_site/all/?$', views.ObservingSiteList.as_view(), name='observingsite-list'),

    url(r'^earth/?$', views.earth_home),
    url(r'^earth/(?P<path>[\s\+0-9a-zA-Z_-]+)/?$', views.earth_home),


    url(r'^accounts/register/$', RegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)

urlpatterns += format_suffix_patterns(urlpatterns)


