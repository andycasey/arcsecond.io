from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.http import HttpResponse

from project.arcsecond import views

if settings.SITE_ID == 3:
    robots_content = ""
else:
    robots_content = "User-agent: *\nDisallow: /"

urlpatterns = patterns('',
    url(r'^$', views.index_www, name='index_www'),
    url('^.*$', views.IndexView.as_view(), name='index'),

    url(r'^robots\.txt$', lambda r: HttpResponse(robots_content)),
    url(r'^admin/', include(admin.site.urls)),

    # The allauth login process first redirect to accounts/profile, which we redirect to @<username>
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile', views.user_account_profile, name='user-account-profile'),
    url(r'^@(?P<username>[\w@\.]+)/$', views.user_profile, name="user-profile"),
    url(r'^@(?P<username>[\w@\.]+)/settings$', views.user_settings, name="user-settings"),
)

if settings.SITE_ID == 2:
    import urls_api
    urlpatterns += patterns('',
        url(r'^api/', include(urls_api.urlpatterns))
    )

handler404 = 'views.custom_404'

