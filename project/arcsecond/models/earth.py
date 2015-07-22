
from django.db import models
from multiselectfield import MultiSelectField
from .constants import *

# **** ASTROPY COMPATIBILITY: 1.0 **** #

class CoordinatesManager(models.Manager):
    def get_by_natural_key(self, longitude, latitude):
        return self.get(longitude=longitude, latitude=latitude)

class Coordinates(models.Model):
    """The minimal set of 3D values to define a location coordinates on Earth.
    See http://docs.astropy.org/en/stable/api/astropy.coordinates.Coordinates.html
    """
    class Meta:
        app_label = 'arcsecond'
        unique_together = (('longitude', 'latitude'),)
        ordering = ["longitude", "latitude"]

    objects = CoordinatesManager()

    longitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    latitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
    height = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)

    def natural_key(self):
        return (self.longitude, self.latitude)

    def are_empty(self):
        return self.longitude == NOT_A_SCIENTIFIC_NUMBER or \
               self.latitude == NOT_A_SCIENTIFIC_NUMBER or \
               self.height == NOT_A_SCIENTIFIC_NUMBER

    def __unicode__(self):
        return u"(long: %.8f, lat: %.8f, h: %.2fm)" % (self.longitude, self.latitude, self.height)

    @classmethod
    def create(cls, longitude, latitude, height, east_positive=True):
        loc = cls()
        loc.longitude = longitude if east_positive is True else -1.0*longitude
        loc.latitude = latitude
        loc.height = height
        return loc


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

    WAVELENGTH_DOMAINS = ((WAVELENGTH_DOMAIN_HARD_GAMMARAYS, "Hard gamma-rays"),
                          (WAVELENGTH_DOMAIN_WEAK_GAMMARAYS, "Weak gamma-rays"),
                          (WAVELENGTH_DOMAIN_HARD_XRAYS, "Hard x-rays"),
                          (WAVELENGTH_DOMAIN_WEAK_XRAYS, "Weak x-rays"),
                          (WAVELENGTH_DOMAIN_FAR_UV, "Far ultraviolet"),
                          (WAVELENGTH_DOMAIN_NEAR_UV, "Near ultraviolet"),
                          (WAVELENGTH_DOMAIN_OPTICAL, "Optical"),
                          (WAVELENGTH_DOMAIN_NEAR_INFRARED, "Near infrared"),
                          (WAVELENGTH_DOMAIN_MID_INFRARED, "Mid-infrared"),
                          (WAVELENGTH_DOMAIN_FAR_INFRARED, "Far infrared"),
                          (WAVELENGTH_DOMAIN_SUBMM, "Sub-milimetric"),
                          (WAVELENGTH_DOMAIN_MM, "Milimetric"),
                          (WAVELENGTH_DOMAIN_RADIO, "Radio"))

    wavelength_domains = MultiSelectField(choices=WAVELENGTH_DOMAINS)

    MOUNTING_EQUATORIAL = "equ"
    MOUNTING_CASSEGRAIN = "cas"
    MOUNTING_ALTAZ = "aaz"

    MOUNTINGS = ((MOUNTING_EQUATORIAL, "Equatorial"),
                 (MOUNTING_CASSEGRAIN, "Cassegrain"),
                 (MOUNTING_ALTAZ, "Alt-Az"))

    mounting = models.CharField(choices=MOUNTINGS, max_length=3)

    OPTICAL_DESIGN_RITCHEY_CHRETIEN = "rc"
    OPTICAL_DESIGN_SCHMIDT = "sc"

    OPTICAL_DESIGNS = ((OPTICAL_DESIGN_RITCHEY_CHRETIEN, u"Ritchey-Chretien"),
                       (OPTICAL_DESIGN_SCHMIDT, u"Schmidt"))

    optical_design = models.CharField(choices=OPTICAL_DESIGNS, max_length=2, null=True, blank=True)


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

    diameter = models.FloatField(null=True, blank=True)
    thickness = models.FloatField(null=True, blank=True)
    shape = models.CharField(max_length=1000, null=True, blank=True)
    curvature = models.CharField(max_length=1000, null=True, blank=True)
    coating = models.CharField(max_length=1000, null=True, blank=True)
    central_obscuration = models.FloatField(null=True, blank=True)
    material = models.CharField(max_length=1000, null=True, blank=True)
    creation_date = models.DateField(null=True, blank=True)
