from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import patterns
from django.conf.urls import url

from project.arcsecond import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^1/objects/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.AstronomicalObjectGETView.as_view(), name='astronomicalobject-detail'),
    url(r'^1/exoplanets/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ExoplanetGETView.as_view(), name="exoplanet-detail"),

    # url(r'^earth/?$', views.earth_home, name="earth-home"),
    # url(r'^earth/browse/?$', views.earth_browse, name="earth-browse"),

    url(r'^1/observingsites/$', views.ObservingSiteList.as_view(), name="observingsite-list"),
    url(r'^1/observingsites/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ObservingSiteDetail.as_view(), name="observingsite-detail"),

    # url(r'^1/observingsites/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ObservingSiteList.as_view(), name="observingsite-list"),

    # url(r'^earth/site/?$', views.ObservingSiteList.as_view(), name='site-list'),
    # url(r'^earth/site/(?P<pk>[0-9]+)/?$', views.ObservingSiteDetail.as_view(), name='site-list'),
    #
    # url(r'^earth/site/coordinates/?$', views.SiteCoordinatesList.as_view(), name='terrestrialcoordinates-list'),
    # url(r'^earth/site/coordinates/(?P<pk>[0-9]+)/?$', views.SiteCoordinatesDetail.as_view(), name='terrestrialcoordinates-detail'),
)

urlpatterns += format_suffix_patterns(urlpatterns)



