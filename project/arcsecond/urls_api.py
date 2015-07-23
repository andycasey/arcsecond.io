from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import patterns
from django.conf.urls import url

from project.arcsecond import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^1/objects/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.AstronomicalObjectAPIView.as_view(), name='astronomicalobject-detail'),

    url(r'^1/exoplanets/$', views.ExoplanetListAPIView.as_view(), name="exoplanet-list"),
    url(r'^1/exoplanets/(?P<pk>\d+)/$', views.ExoplanetDetailAPIView.as_view(), name="exoplanet-detail"),
    url(r'^1/exoplanets/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ExoplanetNamedDetailAPIView.as_view(), name="exoplanet-named-detail"),

    # url(r'^earth/?$', views.earth_home, name="earth-home"),
    # url(r'^earth/browse/?$', views.earth_browse, name="earth-browse"),

    url(r'^1/observingsites/$', views.ObservingSiteListAPIView.as_view(), name="observingsite-list"),
    url(r'^1/observingsites/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ObservingSiteDetailAPIView.as_view(), name="observingsite-detail"),

    # url(r'^1/observingsites/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ObservingSiteListAPIView.as_view(), name="observingsite-list"),

    # url(r'^earth/site/?$', views.ObservingSiteListAPIView.as_view(), name='site-list'),
    # url(r'^earth/site/(?P<pk>[0-9]+)/?$', views.ObservingSiteDetailAPIView.as_view(), name='site-list'),
    #
    # url(r'^earth/site/coordinates/?$', views.SiteCoordinatesList.as_view(), name='terrestrialcoordinates-list'),
    # url(r'^earth/site/coordinates/(?P<pk>[0-9]+)/?$', views.SiteCoordinatesDetail.as_view(), name='terrestrialcoordinates-detail'),
)

urlpatterns += format_suffix_patterns(urlpatterns)



