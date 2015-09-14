from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.http import HttpResponse

from project.arcsecond import views

robots_content = "" if settings.SITE_ID == 3 else "User-agent: *\nDisallow: /"

# The request-based view for the strictly empty URL / of host 'www'.
urlpatterns = patterns('',
    url(r'^$', views.index_www, name='index_www'),
)

# Because we can't have a STAGING sub-subdomain api.arcsecond-staging.herokuapp.com, we put /api behind.
if settings.SITE_ID == 2:
    import urls_api
    urlpatterns += patterns('',
        url(r'^api/', include(urls_api.urlpatterns))
    )

# All remaining non-empty patterns of the 'www'. Order matters! Put the all-catching webapp in last position,
# to ensure all other have a chance to be caught.

urlpatterns += patterns('',
    url(r'^robots\.txt$', lambda r: HttpResponse(robots_content)),
    url(r'^admin/', include(admin.site.urls)),

    # The allauth login process first redirect to accounts/profile, which we redirect to @<username>
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile', views.user_account_profile, name='user-account-profile'),
    url(r'^@(?P<username>[\w@\.]+)/$', views.user_profile, name="user-profile"),
    url(r'^@(?P<username>[\w@\.]+)/settings$', views.user_settings, name="user-settings"),

    # The 'old' Angular piece of code, not using (yet) the service.
    url(r'^observingsites/map?$', views.observingsites_map, name="observingsites-map"),

    url('^.+$', views.ObservingSitesIndexView.as_view(), name='index_observingsites'),
)

handler404 = 'views.custom_404'

