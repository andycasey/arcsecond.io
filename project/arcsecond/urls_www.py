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

    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', lambda r: HttpResponse(robots_content)),

    url(r'^observingsites/?$', views.observingsites, name="observingsites"),
)

if settings.DEBUG:
    import urls_api
    urlpatterns += urls_api.urlpatterns

handler404 = 'views.custom_404'

