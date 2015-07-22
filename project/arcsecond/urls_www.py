from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from project.arcsecond import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^observingsites/?$', views.observingsites, name="observingsites"),

    # url(r'^accounts/profile/?$', views.UserProfileView, name='user-profile'),

    # url(r'^earth/site/?$', views.ObservingSiteListAPIView.as_view(), name='site-list'),
    # url(r'^earth/site/(?P<pk>[0-9]+)/?$', views.ObservingSiteDetailAPIView.as_view(), name='site-list'),
    #
    # url(r'^earth/site/coordinates/?$', views.SiteCoordinatesList.as_view(), name='terrestrialcoordinates-list'),
    # url(r'^earth/site/coordinates/(?P<pk>[0-9]+)/?$', views.SiteCoordinatesDetail.as_view(), name='terrestrialcoordinates-detail'),
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^1/exoplanets_debug/$', views.ExoplanetListAPIView.as_view(), name="exoplanet-list"))
    urlpatterns += patterns('', url(r'^1/exoplanets_debug/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ExoplanetDetailAPIView.as_view(), name="exoplanet-detail"))

    urlpatterns += patterns('', url(r'^1/objects_debug/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.AstronomicalObjectAPIView.as_view(), name='astronomicalobject-detail'))

    urlpatterns += patterns('', url(r'^1/observingsites_debug/$', views.ObservingSiteListAPIView.as_view(), name="observingsite-list"))
    urlpatterns += patterns('', url(r'^1/observingsites_debug/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ObservingSiteDetailAPIView.as_view(), name="observingsite-detail"))

    urlpatterns += patterns('', url(r'^1/coordinates_debug/(?P<pk>\d+)/$', views.CoordinatesDetailAPIView.as_view(), name="coordinates-detail"))

urlpatterns += format_suffix_patterns(urlpatterns)


handler404 = 'views.custom_404'

