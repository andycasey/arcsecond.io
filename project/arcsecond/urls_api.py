from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import patterns
from django.conf.urls import url

from project.arcsecond import views
from project.arcsecond.models import constants

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^1/objects/(?P<name>[\s\+0-9a-zA-Z_-]+)/$',
        views.AstronomicalObjectAPIView.as_view(),
        name='astronomicalobject-detail'),

    url(r'^1/exoplanets/$',
        views.ExoplanetListAPIView.as_view(),
        name="exoplanet-list"),

    url(r'^1/exoplanets/(?P<pk>\d+)/$',
        views.ExoplanetDetailAPIView.as_view(),
        name="exoplanet-detail"),

    url(r'^1/exoplanets/(?P<name>[\s\+0-9a-zA-Z_-]+)/$',
        views.ExoplanetNamedDetailAPIView.as_view(),
        name="exoplanet-named-detail"),

    url(r'^1/observingsites/$',
        views.ObservingSiteListAPIView.as_view(),
        name="observingsite-list"),

    url(r'^1/observingsites/(?P<name>[\s\+0-9a-zA-Z_-]+)/$',
        views.ObservingSiteDetailAPIView.as_view(),
        name="observingsite-detail"),

    url(r'^1/archives/ESO/(?P<programme_id>'+constants.eso_programme_id_regex+')/summary/$',
        views.ESOProgrammeSummaryDetailAPIView.as_view(),
        name="esoprogrammesummary-detail"),

    url(r'^1/archives/HST/(?P<programme_id>[0-9]+)/summary/$',
        views.HSTProgrammeSummaryDetailAPIView.as_view(),
        name="hstprogrammesummary-detail"),
)

urlpatterns += format_suffix_patterns(urlpatterns)



