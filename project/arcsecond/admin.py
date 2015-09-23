from django.contrib import admin
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

from project.arcsecond.models import *

# Augmented Site Admin
class WebSiteAdmin(SiteAdmin):
    list_display = ("pk", "domain", "name")

admin.site.unregister(Site)
admin.site.register(Site, WebSiteAdmin)

# Register your models here.

@admin.register(ObservingSite)
class ObservingSiteAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "state_province", "country", "IAUCode", "coordinates")

@admin.register(ObservingSiteActivity)
class ObservingSiteActivityAdmin(admin.ModelAdmin):
    list_display = ("pk", "date", "user", "observing_site", "action", "property_name", "old_value", "new_value", "action_message", "method")

@admin.register(DataArchive)
class ObservingSiteAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "url")
