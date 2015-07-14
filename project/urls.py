
from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('project.iobserve.urls', namespace="www")),
    url(r'^', include('project.iobserve.urls_api', namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)

handler404 = 'iobserve.views.custom_404'

