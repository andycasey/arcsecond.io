
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^', include('project.iobserve.urls', namespace="iobserve")),
  url(r'^admin/', include(admin.site.urls)),
)
