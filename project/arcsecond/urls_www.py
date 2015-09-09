from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import RedirectView
from project.arcsecond import views

if settings.SITE_ID == 3:
    robots_content = ""
else:
    robots_content = "User-agent: *\nDisallow: /"

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^onekilopars.ec$', RedirectView.as_view(url="/", permanent=True)),
    url(r'^robots\.txt$', lambda r: HttpResponse(robots_content)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^@(?P<username>[\w]+)/$', views.user_profile, name="user-profile"),
    url(r'^@(?P<username>[\w]+)/settings$', views.user_settings, name="user-settings"),
    url(r'^accounts/profile', views.user_account_profile, name='user-account-profile'),
    url(r'^observingsites/?$', views.observingsites, name="observingsites"),
    # url(r'^telescopes/?$', views.telescopes, name="telescopes"),

    # CORS HEADERS SOLUTION PENDING

    url(r'^1/observingsites/$',
        views.ObservingSiteListAPIView.as_view(),
        name="www-observingsite-list"),

    # url(r'^1/telescopes/$',
    #     views.TelescopeListAPIView.as_view(),
    #     name="www-telescope-list"),
)

if settings.DEBUG is True:
    import urls_api
    urlpatterns += urls_api.urlpatterns

handler404 = 'views.custom_404'

