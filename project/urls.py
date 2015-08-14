
from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('project.arcsecond.urls_www', namespace="www")),
    url(r'^', include('project.arcsecond.urls_api', namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
)

