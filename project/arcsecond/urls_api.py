from django.conf import settings
from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from project.arcsecond import views
from project.arcsecond.models import constants

full_string_regex = "[\s\d\w().+-_',:&]+"

urlpatterns = patterns('',
    url(r'^$', views.index_api, name='index_api'),
    url(r'^accounts/', include('allauth.urls')),

    # ----- Objects -----

    url(r'^1/objects/(?P<name>'+full_string_regex+')/$',
        views.AstronomicalObjectDetailAPIView.as_view(),
        name='astronomicalobject-detail'),


    # ----- Exoplanets -----

    url(r'^1/exoplanets/$',
        views.ExoplanetListAPIView.as_view(),
        name="exoplanet-list"),

    url(r'^1/exoplanets/(?P<pk>\d+)/$',
        views.ExoplanetDetailAPIView.as_view(),
        name="exoplanet-detail"),

    url(r'^1/exoplanets/(?P<name>'+full_string_regex+')/$',
        views.ExoplanetNamedDetailAPIView.as_view(),
        name="exoplanet-named-detail"),


    # ----- Observing Sites -----

    url(r'^1/observingsites/$',
        views.ObservingSiteListAPIView.as_view(),
        name="observingsite-list"),

    url(r'^1/observingsites/activities$',
        views.ObservingSiteActivityListAPIView.as_view(),
        name="observingsiteactivity-list"),

    url(r'^1/observingsites/(?P<name>'+full_string_regex+')/$',
        views.ObservingSiteNamedDetailAPIView.as_view(),
        name="observingsite-named-detail"),


    # ----- Telescopes -----

    url(r'^1/telescopes/(?P<pk>\d+)/$',
        views.TelescopeDetailAPIView.as_view(),
        name="telescope-detail"),

    # url(r'^1/telescopes/(?P<name>'+full_string_regex+')/$',
    #     views.TelescopeDetailAPIView.as_view(),
    #     name="telescope-detail"),

    url(r'^1/telescopes/$',
        views.TelescopeListAPIView.as_view(),
        name="telescope-list"),


    # ----- Telegrams -----

    url(r'^1/telegrams/ATel/(?P<identifier>\d+)/$',
        views.AstronomersTelegramDetailAPIView.as_view(),
        name="astronomerstelegram-detail"),

    url(r'^1/telegrams/ATel/$',
        views.AstronomersTelegramListAPIView.as_view(),
        name="astronomerstelegram-list"),

    url(r'^1/telegrams/GCN/Circulars/(?P<identifier>\d+)/$',
        views.GCNCircularDetailAPIView.as_view(),
        name="gcncircular-detail"),


    # ----- Publications -----

    url(r'^1/publications/(?P<bibcode>'+constants.bibcode_regex+')$',
        views.PublicationDetailAPIView.as_view(),
        name="publication-detail"),


    # ----- People -----

    url(r'^1/people/(?P<name>'+full_string_regex+')/$',
        views.PersonDetailAPIView.as_view(),
        name="person-detail"),


    # ----- Archives -----

    url(r'^1/archives/ESO/$',
        views.ESOArchiveDataRowsListAPIView.as_view(),
        name="esoarchivedatarow-detail"),

    url(r'^1/archives/ESO/(?P<programme_id>'+constants.eso_programme_id_regex+')/summary/$',
        views.ESOProgrammeSummaryDetailAPIView.as_view(),
        name="esoprogrammesummary-detail"),

    url(r'^1/archives/HST/(?P<programme_id>[0-9]+)/summary/$',
        views.HSTProgrammeSummaryDetailAPIView.as_view(),
        name="hstprogrammesummary-detail"),


    # ----- Finding Charts -----

    url(r'^1/findingcharts/(?P<input>'+full_string_regex+')/$',
        views.FindingChartListAPIView.as_view(),
        name="findingchart-list"),


    # ----- Converters -----

    url(r'^1/converters/coordinates/ra/(?P<ra>[\+\.\:0-9]+)/dec/(?P<dec>[-\.\:0-9]+)/$',
        views.CoordinatesConverterDetailAPIView.as_view(),
        name="coordinatesconversion-detail"),


    url(r'^1/converters/times/(?P<input_format>'+constants.time_formats_regex+')/(?P<input_value>[-+.:0-9A-Z]+)/$',
        views.TimesDetailAPIView.as_view(),
        name="timesconversion-detail"),
)

if settings.SITE_ID == 2:
    urlpatterns += patterns('',
        url(r'^api/$', views.index_api, name='index_api'),
    )

if settings.DEBUG == False:
    urlpatterns += format_suffix_patterns(urlpatterns)



