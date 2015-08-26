from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from project.arcsecond import views
from project.arcsecond.models import constants

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # ----- Objects -----

    url(r'^1/objects/(?P<name>[\s\+\.0-9a-zA-Z_-]+)/$',
        views.AstronomicalObjectDetailAPIView.as_view(),
        name='astronomicalobject-detail'),


    # ----- Exoplanets -----

    url(r'^1/exoplanets/$',
        views.ExoplanetListAPIView.as_view(),
        name="exoplanet-list"),

    url(r'^1/exoplanets/(?P<pk>\d+)/$',
        views.ExoplanetDetailAPIView.as_view(),
        name="exoplanet-detail"),

    url(r'^1/exoplanets/(?P<name>[\(\)\.\'\s\+0-9a-zA-Z_-]+)/$',
        views.ExoplanetNamedDetailAPIView.as_view(),
        name="exoplanet-named-detail"),


    # ----- Observing Sites -----

    url(r'^1/observingsites/(?P<name>[\s\+\.0-9a-zA-Z_-]+)/$',
        views.ObservingSiteDetailAPIView.as_view(),
        name="observingsite-detail"),

    url(r'^1/observingsites/$',
        views.ObservingSiteListAPIView.as_view(),
        name="observingsite-list"),


    # ----- Telegrams -----

    url(r'^1/telegrams/ATel/(?P<identifier>\d+)/$',
        views.AstronomersTelegramDetailAPIView.as_view(),
        name="astronomerstelegram-detail"),

    url(r'^1/telegrams/ATel/$',
        views.AstronomersTelegramListAPIView.as_view(),
        name="astronomerstelegram-list"),


    # ----- Publications -----

    url(r'^1/publications/(?P<bibcode>'+constants.bibcode_regex+')$',
        views.PublicationDetailAPIView.as_view(),
        name="publication-detail"),


    # ----- People -----

    url(r'^1/people/(?P<name>[A-Za-z\.\+]+)/$',
        views.PersonDetailAPIView.as_view(),
        name="person-detail"),


    # ----- Archives -----

    url(r'^1/archives/ESO/(?P<programme_id>'+constants.eso_programme_id_regex+')/summary/$',
        views.ESOProgrammeSummaryDetailAPIView.as_view(),
        name="esoprogrammesummary-detail"),

    url(r'^1/archives/HST/(?P<programme_id>[0-9]+)/summary/$',
        views.HSTProgrammeSummaryDetailAPIView.as_view(),
        name="hstprogrammesummary-detail"),


    # ----- Finding Charts -----

    url(r'^1/findingcharts/(?P<input>[\(\)\,\:\s\+\-\.0-9a-zA-Z_]+)/$',
        views.FindingChartListAPIView.as_view(),
        name="findingchart-list"),


    # ----- Converters -----

    url(r'^1/converters/coordinates/ra/(?P<ra>[\+\.\:0-9]+)/dec/(?P<dec>[-\.\:0-9]+)/$',
        views.CoordinatesConverterDetailAPIView.as_view(),
        name="coordinatesconversion-detail"),


    url(r'^1/converters/times/(?P<input_format>'+constants.time_formats_regex+')/(?P<input_value>[\-\+\.\:0-9A-Z]+)/$',
        views.TimesDetailAPIView.as_view(),
        name="timesconversion-detail"),
)

if settings.DEBUG == False:
    urlpatterns += format_suffix_patterns(urlpatterns)



