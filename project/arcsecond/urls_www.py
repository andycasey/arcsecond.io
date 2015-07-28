from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from models import constants

from project.arcsecond import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^observingsites/?$', views.observingsites, name="observingsites"),
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^1/exoplanets/$', views.ExoplanetListAPIView.as_view(), name="exoplanet-list"))
    urlpatterns += patterns('', url(r'^1/exoplanets/(?P<pk>\d+)/$', views.ExoplanetDetailAPIView.as_view(), name="exoplanet-detail"))
    urlpatterns += patterns('', url(r'^1/exoplanets/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ExoplanetNamedDetailAPIView.as_view(), name="exoplanet-named-detail"))

    urlpatterns += patterns('', url(r'^1/objects/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.AstronomicalObjectAPIView.as_view(), name='astronomicalobject-detail'))

    urlpatterns += patterns('', url(r'^1/observingsites/$', views.ObservingSiteListAPIView.as_view(), name="observingsite-list"))
    urlpatterns += patterns('', url(r'^1/observingsites/(?P<name>[\s\+0-9a-zA-Z_-]+)/$', views.ObservingSiteDetailAPIView.as_view(), name="observingsite-detail"))

    urlpatterns += patterns('', url(r'^1/coordinates/(?P<pk>\d+)/$', views.CoordinatesDetailAPIView.as_view(), name="coordinates-detail"))

    urlpatterns += patterns('', url(r'^1/archives/ESO/(?P<programme_id>'+constants.eso_programme_id_regex+')/summary/$',
        views.ESOProgrammeSummaryDetailAPIView.as_view(),
        name="esoprogrammesummary-detail"))

    urlpatterns += patterns('', url(r'^1/archives/HST/(?P<programme_id>[0-9]+)/summary/$',
        views.HSTProgrammeSummaryDetailAPIView.as_view(),
        name="hstprogrammesummary-detail"))

urlpatterns += format_suffix_patterns(urlpatterns)


handler404 = 'views.custom_404'

