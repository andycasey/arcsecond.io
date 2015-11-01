# coding=utf-8

from django.conf import settings
from django.contrib import auth
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from .earth import *

class ObservingSiteManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class ObservingSite(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = ObservingSiteManager()

    name = models.CharField(max_length=100, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    alternate_name_1 = models.CharField(max_length=100, null=True, blank=True)
    alternate_name_2 = models.CharField(max_length=100, null=True, blank=True)
    acronym = models.CharField(max_length=100, null=True, blank=True, unique=True)

    IAUCode = models.CharField(max_length=200, null=True, blank=True, unique=True)

    CONTINENT_UNDEFINED = "(Undefined)"
    CONTINENT_ASIA = "Asia"
    CONTINENT_AFRICA = "Africa"
    CONTINENT_ANTARCTICA = "Antarctica"
    CONTINENT_EUROPE = "Europe"
    CONTINENT_NORTH_AMERICA = "North America"
    CONTINENT_OCEANIA = "Oceania"
    CONTINENT_SOUTH_AMERICA = "South America"

    CONTINENTS_TYPES_CHOICES = (
        (CONTINENT_UNDEFINED, '(Undefined)'),
        (CONTINENT_ASIA, 'Asia'),
        (CONTINENT_AFRICA, 'Africa'),
        (CONTINENT_ANTARCTICA, 'Antarctica'),
        (CONTINENT_EUROPE, 'Europe'),
        (CONTINENT_NORTH_AMERICA, 'North America'),
        (CONTINENT_OCEANIA, 'Oceania'),
        (CONTINENT_SOUTH_AMERICA, 'South America'),
    )

    continent = models.CharField(max_length=100, choices=CONTINENTS_TYPES_CHOICES, default=CONTINENT_UNDEFINED)
    coordinates = models.OneToOneField(Coordinates, null=True, related_name="site")

    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    state_province = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)

    time_zone = models.CharField(max_length=200, null=True, blank=True)
    time_zone_name = models.CharField(max_length=200, null=True, blank=True)

    homepage = models.URLField(null=True, blank=True)
    wikipedia_article = models.URLField(null=True, blank=True)

    SOURCE_UNDEFINED = "(Undefined)"
    SOURCE_USER = "User"
    SOURCE_IOBSERVE = "iObserve"
    SOURCE_XEPHEM = "Xephem"
    SOURCE_MPC = "MPC"

    SOURCE_KEYS = (
        SOURCE_UNDEFINED,
        SOURCE_USER,
        SOURCE_IOBSERVE,
        SOURCE_XEPHEM,
        SOURCE_MPC
    )

    SOURCE_VALUES = SOURCE_KEYS
    SOURCE_CHOICES = tuple(zip(SOURCE_KEYS, SOURCE_VALUES))
    sources = MultiSelectField(choices=SOURCE_CHOICES, null=True, blank=True)

    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def natural_key(self):
        return (self.name,)

    def __unicode__(self):
        return u"<ObservingSite {0} ({1}, {2}) [{3}]>".format(self.name, self.state_province, self.country, self.coordinates)


class ObservingSiteActivity(models.Model):
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='observingsite_activities')
    observing_site = models.ForeignKey(ObservingSite, null=True, blank=True, related_name='activities')

    ACTION_UNDEFINED = "unk"
    ACTION_LOAD = "load"
    ACTION_PROPERTY_CHANGE = "prop"
    ACTION_SITE_DELETION = "del"

    ACTION_KEYS = (ACTION_UNDEFINED, ACTION_LOAD, ACTION_PROPERTY_CHANGE, ACTION_SITE_DELETION)
    ACTION_VALUES = ("(Undefined)", "loaded", "changed property", "deleted site")
    ACTION_CHOICES = tuple(zip(ACTION_KEYS, ACTION_VALUES))
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, default=ACTION_UNDEFINED)

    property_name = models.CharField(max_length=200, null=True, blank=True)
    old_value = models.CharField(max_length=200, null=True, blank=True)
    new_value = models.CharField(max_length=200, null=True, blank=True)
    action_message = models.CharField(max_length=1000, null=True, blank=True)

    METHOD_UNDEFINED = "unk"
    METHOD_DB = "db"
    METHOD_DJANGO = "django"
    METHOD_API = "api"
    METHOD_WEB = "web"

    METHOD_KEYS = (METHOD_UNDEFINED, METHOD_DB, METHOD_DJANGO, METHOD_API, METHOD_WEB)
    METHOD_VALUES = METHOD_KEYS
    METHOD_CHOICES = tuple(zip(METHOD_KEYS, METHOD_VALUES))
    method = models.CharField(max_length=10, choices=METHOD_CHOICES, default=METHOD_UNDEFINED)



class AstronomicalOrganisationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class AstronomicalOrganisation(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = AstronomicalOrganisationManager()

    name = models.CharField(max_length=100, null=True, blank=True)
    acronym = models.CharField(max_length=100, null=True, blank=True)

    # headquarters = models.OneToOneField(ObservingSite, related_name="astronomical_organisation", null=True, blank=True)
    observing_sites = models.ManyToManyField(ObservingSite, related_name="astronomical_organisations")

    website = models.URLField(null=True, blank=True)
    wikipedia_article = models.URLField(null=True, blank=True)

    ORGANISATION_TYPE_UNKNOWN = "Unknown"
    ORGANISATION_TYPE_PUBLIC = "Public"
    ORGANISATION_TYPE_PRIVATE = "Private"
    ORGANISATION_TYPE_MIXED = "Mixed"

    ORGANISATION_TYPES_CHOICES = (
        (ORGANISATION_TYPE_UNKNOWN, 'Unknown'),
        (ORGANISATION_TYPE_PUBLIC, 'Public'),
        (ORGANISATION_TYPE_PRIVATE, 'Private'),
        (ORGANISATION_TYPE_MIXED, 'Mixed'),
    )

    organisation_type = models.CharField(max_length=100, choices=ORGANISATION_TYPES_CHOICES, default=ORGANISATION_TYPE_UNKNOWN)

    def natural_key(self):
        return (self.name,)
