from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic.base import RedirectView

from arcsecond import views

robots_content = "" if settings.SITE_ID == 3 else "User-agent: *\nDisallow: /"

# The request-based view for the strictly empty URL / of host 'www'.
urlpatterns = patterns('',
    url(r'^robots\.txt$', lambda r: HttpResponse(robots_content)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^privacy', views.privacy_policy, name='privacy-policy'),

    url(r'^auth/registration/account-confirm-email/(?P<key>\w+)/$', views.AccountConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth/', include('rest_auth.urls')),

    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^rest-auth/twitter/$', views.TwitterLogin.as_view(), name='tw_login')


    # The allauth login process first redirect to accounts/profile, which we redirect to @<username>
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/profile/$', RedirectView.as_view(url='/'), name='profile-redirect'),
    # url(r'^accounts/profile', views.user_account_profile, name='user-account-profile'),
    # url(r'^users/(?P<username>[\w@\.]+)$', views.user_profile, name="user-profile"),
    # url(r'^users/(?P<username>[\w@\.]+)/settings$', views.user_settings, name="user-settings"),

    url(r'^.*$', views.IndexView.as_view(), name='index_www'),
    url(r'^.*/$', views.IndexView.as_view(), name='index_www'),
)


# Because we can't have a STAGING sub-subdomain api.arcsecond-staging.herokuapp.com, we put /api behind.
if settings.SITE_ID == 2:
    import urls_api
    urlpatterns += patterns('',
        url(r'^api/', include(urls_api.urlpatterns))
    )


handler404 = 'views.custom_404'

