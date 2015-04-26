
# **** ASTROPY COMPATIBILITY: 1.0 **** #

from .constants import *
from .common import *


class CoordinatesManager(models.Manager):
    def get_by_natural_key(self, longitude, latitude):
        return self.get(longitude=longitude, latitude=latitude)


# The minimal set of 3D values to define a location coordinates on Earth.
# See http://docs.astropy.org/en/stable/api/astropy.coordinates.Coordinates.html
class Coordinates(models.Model):
    objects = CoordinatesManager()

    class Meta:
        app_label = 'iobserve'
        unique_together = (('longitude', 'latitude'),)
        ordering = ["longitude", "latitude"]

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


class SiteManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Site(models.Model):
    objects = SiteManager()

    class Meta:
        app_label = 'iobserve'

    name = models.CharField(max_length=100, primary_key=True)
    long_name = models.CharField(max_length=100, null=True, blank=True)

    CONTINENT_UNDEFINED = "(Undefined)"
    CONTINENT_ASIA = "Asia"
    CONTINENT_ANTARCTICA = "Antarctica"
    CONTINENT_EUROPE = "Europe"
    CONTINENT_NORTH_AMERICA = "North America"
    CONTINENT_OCEANIA = "Oceania"
    CONTINENT_SOUTH_AMERICA = "South America"

    CONTINENTS_TYPES_CHOICES = (
        (CONTINENT_UNDEFINED, '(Undefined)'),
        (CONTINENT_ASIA, 'Asia'),
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
    natural_key.dependencies = ['iobserve.coordinates']



class ObservingSiteManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class ObservingSite(Site):
    objects = ObservingSiteManager()

    class Meta:
        app_label = 'iobserve'

    IAUCode = models.CharField(max_length=200, null=True, blank=True)

class AstronomicalOrganisationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class AstronomicalOrganisation(models.Model):
    objects = AstronomicalOrganisationManager()

    class Meta:
        app_label = 'iobserve'

    name = models.CharField(max_length=100, primary_key=True)
    acronym = models.CharField(max_length=100, null=True)

    headquarters = models.OneToOneField(Site, related_name="astronomical_organisation", null=True, blank=True)
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

