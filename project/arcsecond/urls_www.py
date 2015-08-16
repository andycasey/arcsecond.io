from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import RedirectView
from .views import *

if settings.SITE_ID == 3:
    robots_content = ""
else:
    robots_content = "User-agent: *\nDisallow: /"

urlpatterns = patterns('',
    url(r'^$', index, name='index'),

    url(r'^onekilopars.ec$', RedirectView.as_view(url="/", permanent=True)),
    url(r'^robots\.txt$', lambda r: HttpResponse(robots_content)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^@(?P<username>[\w]+)/$', user_profile, name="user-profile"),
    url(r'^@(?P<username>[\w]+)/settings$', user_settings, name="user-settings"),
    url(r'^accounts/profile', user_account_profile, name='user-account-profile'),
    url(r'^observingsites/?$', observingsites, name="observingsites"),
)

if settings.DEBUG is True:
    import urls_api
    urlpatterns += urls_api.urlpatterns

handler404 = 'views.custom_404'

