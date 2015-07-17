from django.contrib import admin
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

# Register your models here.

class WebSiteAdmin(SiteAdmin):
    list_display = ("pk", "domain", "name")

admin.site.unregister(Site)
admin.site.register(Site, WebSiteAdmin)

