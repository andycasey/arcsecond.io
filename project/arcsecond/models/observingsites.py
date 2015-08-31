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

    name = models.CharField(max_length=100, primary_key=True)
    long_name = models.CharField(max_length=100, null=True, blank=True)
    IAUCode = models.CharField(max_length=200, null=True, blank=True)

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
    country = models.CharField(max_length=200, null=True)

    time_zone = models.CharField(max_length=200, null=True, blank=True)
    time_zone_name = models.CharField(max_length=200, null=True, blank=True)

    homepage = models.URLField(null=True, blank=True)
    wikipedia_article = models.URLField(null=True, blank=True)

    @classmethod
    def create(cls, name, longitude, latitude, height, east_positive=True):
        site = cls(name=name)
        earth_location = Coordinates.create(longitude, latitude, height, east_positive)
        site.earth_location = earth_location
        site.displayed_name = site.name
        return site

    def natural_key(self):
        return (self.name,) + self.coordinates.natural_key()
    natural_key.dependencies = ['arcsecond.coordinates']


class AstronomicalOrganisationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class AstronomicalOrganisation(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = AstronomicalOrganisationManager()

    name = models.CharField(max_length=100, primary_key=True)
    acronym = models.CharField(max_length=100, null=True)

    headquarters = models.OneToOneField(ObservingSite, related_name="astronomical_organisation", null=True, blank=True)
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

    organisation_type = models.CharField(max_length=100,
                                         choices=ORGANISATION_TYPES_CHOICES,
                                         default=ORGANISATION_TYPE_UNKNOWN)


class BuildingManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Building(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = BuildingManager()
    name = models.CharField(max_length=1000, primary_key=True)
    coordinates = models.ManyToManyField(Coordinates, blank=True, related_name="building")


class DomeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Dome(Building):
    class Meta: app_label = 'arcsecond'
    objects = DomeManager()


class ToolManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Tool(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = ToolManager()
    name = models.CharField(max_length=1000, primary_key=True)
    acronym = models.CharField(max_length=100, null=True, blank=True)


class ObservingToolManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class ObservingTool(Tool):
    class Meta: app_label = 'arcsecond'
    objects = ObservingToolManager()
    coordinates = models.ManyToManyField(Coordinates, related_name="observing_tool")


class TelescopeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Telescope(ObservingTool):
    class Meta: app_label = 'arcsecond'
    objects = TelescopeManager()
    dome = models.OneToOneField(Dome, blank=True, null=True, default=None, related_name='telescope')

    WAVELENGTH_DOMAIN_HARD_GAMMARAYS = "hga"
    WAVELENGTH_DOMAIN_WEAK_GAMMARAYS = "wga"
    WAVELENGTH_DOMAIN_HARD_XRAYS = "hxr"
    WAVELENGTH_DOMAIN_WEAK_XRAYS = "wxr"
    WAVELENGTH_DOMAIN_FAR_UV = "fuv"
    WAVELENGTH_DOMAIN_NEAR_UV = "nuv"
    WAVELENGTH_DOMAIN_OPTICAL = "opt"
    WAVELENGTH_DOMAIN_NEAR_INFRARED = "nir"
    WAVELENGTH_DOMAIN_MID_INFRARED = "mir"
    WAVELENGTH_DOMAIN_FAR_INFRARED = "fir"
    WAVELENGTH_DOMAIN_SUBMM = "smm"
    WAVELENGTH_DOMAIN_MM = "mmc"
    WAVELENGTH_DOMAIN_RADIO = "rad"

    WAVELENGTH_DOMAIN_KEYS = (
        WAVELENGTH_DOMAIN_HARD_GAMMARAYS,
        WAVELENGTH_DOMAIN_WEAK_GAMMARAYS,
        WAVELENGTH_DOMAIN_HARD_XRAYS,
        WAVELENGTH_DOMAIN_WEAK_XRAYS,
        WAVELENGTH_DOMAIN_FAR_UV,
        WAVELENGTH_DOMAIN_NEAR_UV,
        WAVELENGTH_DOMAIN_OPTICAL,
        WAVELENGTH_DOMAIN_NEAR_INFRARED,
        WAVELENGTH_DOMAIN_MID_INFRARED,
        WAVELENGTH_DOMAIN_FAR_INFRARED,
        WAVELENGTH_DOMAIN_SUBMM,
        WAVELENGTH_DOMAIN_MM,
        WAVELENGTH_DOMAIN_RADIO
    )

    WAVELENGTH_DOMAINS_VALUES = (
        "Hard gamma-rays",
        "Weak gamma-rays",
        "Hard x-rays",
        "Weak x-rays",
        "Far ultraviolet",
        "Near ultraviolet",
        "Optical",
        "Near infrared",
        "Mid-infrared",
        "Far infrared",
        "Sub-milimetric",
        "Milimetric",
        "Radio"
    )

    WAVELENGTH_DOMAINS_CHOICES = tuple(zip(WAVELENGTH_DOMAIN_KEYS, WAVELENGTH_DOMAINS_VALUES))
    wavelength_domains = MultiSelectField(choices=WAVELENGTH_DOMAINS_CHOICES)

    MOUNTING_UNDEFINED = "unk"
    MOUNTING_EQUATORIAL = "equ"
    MOUNTING_CASSEGRAIN = "cas"
    MOUNTING_ALTAZ = "aaz"
    MOUNTING_OFF_AXIS = "off"

    MOUNTINGS_KEYS = (
        MOUNTING_UNDEFINED,
        MOUNTING_EQUATORIAL,
        MOUNTING_CASSEGRAIN,
        MOUNTING_ALTAZ,
        MOUNTING_OFF_AXIS
    )

    MOUNTINGS_VALUES = (
        "Unknown",
        "Equatorial"
        "Cassegrain",
        "Alt-Az",
        "Off-Axis"
    )

    MOUNTING_CHOICES = tuple(zip(MOUNTINGS_KEYS, MOUNTINGS_VALUES))
    mounting = models.CharField(choices=MOUNTING_CHOICES, max_length=3, blank=True, default=MOUNTING_UNDEFINED)

    OPTICAL_DESIGN_UNDEFINED = "unk"
    OPTICAL_DESIGN_RITCHEY_CHRETIEN = "rc"
    OPTICAL_DESIGN_SCHMIDT = "sc"

    OPTICAL_DESIGNS_KEYS = (
        OPTICAL_DESIGN_UNDEFINED,
        OPTICAL_DESIGN_RITCHEY_CHRETIEN,
        OPTICAL_DESIGN_SCHMIDT
    )

    OPTICAL_DESIGNS_VALUES = (
        u"Unknown",
        u"Ritchey-Chrétien",
        u"Schmidt"
    )

    OPTICAL_DESIGNS_CHOICES = tuple(zip(OPTICAL_DESIGNS_KEYS, OPTICAL_DESIGNS_VALUES))
    optical_design = models.CharField(choices=OPTICAL_DESIGNS_CHOICES, max_length=2, default=OPTICAL_DESIGN_UNDEFINED, blank=True)

    has_active_optics = models.NullBooleanField()
    has_adaptative_optics = models.NullBooleanField()
    has_laser_guide_star = models.NullBooleanField()


class ToolComponentManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class ToolComponent(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = ToolComponentManager()
    name = models.CharField(max_length=1000, primary_key=True)

class Mirror(ToolComponent):
    class Meta: app_label = 'arcsecond'
    telescope = models.ForeignKey(Telescope, blank=True, null=True, default=None, related_name='mirrors')

    mirror_index = models.IntegerField(null=True, blank=True, default=0)
    diameter = models.FloatField(null=True, blank=True)
    thickness = models.FloatField(null=True, blank=True)
    shape = models.CharField(max_length=1000, null=True, blank=True)
    curvature = models.CharField(max_length=1000, null=True, blank=True)
    coating = models.CharField(max_length=1000, null=True, blank=True)
    central_obscuration = models.FloatField(null=True, blank=True)
    material = models.CharField(max_length=1000, null=True, blank=True)
    creation_date = models.DateField(null=True, blank=True)
