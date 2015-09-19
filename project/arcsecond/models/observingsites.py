# coding=utf-8
from django.db import models
from multiselectfield import MultiSelectField
from .earth import *

class ObservingSiteManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class ObservingSite(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = ObservingSiteManager()

    short_name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
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
    coordinates = models.OneToOneField(Coordinates, related_name="site")

    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    state_province = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)

    time_zone = models.CharField(max_length=200, null=True, blank=True)
    time_zone_name = models.CharField(max_length=200, null=True, blank=True)

    homepage = models.URLField(null=True, blank=True)
    wikipedia_article = models.URLField(null=True, blank=True)

    def natural_key(self):
        return (self.name,)


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
