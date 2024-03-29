from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic.base import RedirectView

from project.arcsecond import views

robots_content = "" if settings.SITE_ID == 3 else "User-agent: *\nDisallow: /"

# The request-based view for the strictly empty URL / of host 'www'.
urlpatterns = patterns('',
    url(r'^robots\.txt$', lambda r: HttpResponse(robots_content)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^privacy', views.privacy_policy, name='privacy-policy'),

    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),

    url(r'^accounts/login/$', views.IndexView.as_view(), name='account_login'),
    url(r'^accounts/register/$', views.IndexView.as_view(), name='account_signup'),

    url(r'^accounts/', include('allauth.urls')),
)

# Because we can't have a STAGING sub-subdomain api.arcsecond-staging.herokuapp.com, we put /api behind.
if settings.SITE_ID == 2:
    import urls_api
    urlpatterns += patterns('',
        url(r'^api/', include(urls_api.urlpatterns))
    )

# Angular WebApp

urlpatterns += patterns('',
    url(r'^.*$', views.IndexView.as_view(), name='index_www'),
    url(r'^.*/$', views.IndexView.as_view(), name='index_www'),
)


handler404 = 'views.custom_404'

