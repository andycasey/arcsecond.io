from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView

from project.arcsecond import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='arcsecond/robots.txt', mimetype='text/plain')),
    url(r'^observingsites/?$', views.observingsites, name="observingsites"),
)

if settings.DEBUG:
    import urls_api
    urlpatterns += urls_api.urlpatterns

handler404 = 'views.custom_404'

