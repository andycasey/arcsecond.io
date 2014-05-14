
from django.db import models
from constants import *
from common import *

class TerrestrialCoordinatesManager(models.Manager):
  def get_by_natural_key(self, longitude, latitude):
    return self.get(longitude=longitude, latitude=latitude)

# The minimal set of 3D values to define a location coordinates on Earth.
class TerrestrialCoordinates(models.Model):
  objects = TerrestrialCoordinatesManager()

  class Meta:
    app_label = 'iobserve'
    unique_together = (('longitude', 'latitude'),)
    ordering = ["longitude", "latitude"]

  longitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  latitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  altitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  east_positive = models.BooleanField(default=True)

  def natural_key(self):
    return (self.longitude, self.latitude)

  def are_empty(self):
    return self.longitude == NOT_A_SCIENTIFIC_NUMBER or \
        self.latitude == NOT_A_SCIENTIFIC_NUMBER or \
        self.altitude == NOT_A_SCIENTIFIC_NUMBER
      
  def __unicode__(self):
    return u"(long: %.8f, lat: %.8f, alt: %.2fm)"%(self.longitude, self.latitude, self.altitude)
   
  @classmethod
  def create(cls, longitude, latitude, altitude, east_positive=True):
    coords = cls()
    coords.longitude = longitude
    coords.latitude = latitude
    coords.altitude = altitude
    coords.east_positive = east_positive
    return coords


class EarthLocationManager(models.Manager):
  def get_by_natural_key(self, name):
    return self.get(name=name)
   
class EarthLocation(models.Model):
  objects = EarthLocationManager()

  class Meta:
    app_label = 'iobserve'
    ordering = ["name"]
    abstract = True

  name = models.CharField(max_length=100, primary_key=True)
  coordinates = models.OneToOneField(TerrestrialCoordinates, related_name="%(app_label)s_%(class)s_related")

  def natural_key(self):
    return (self.name,) + self.coordinates.natural_key()
  natural_key.dependencies = ['iobserve.terrestrialcoordinates']

  def __unicode__(self):
    return "%s (%s, %s)"%(self, self.name, self.coordinates)



class Site(EarthLocation):
  class Meta:
    app_label = 'iobserve'
  
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

  long_name = models.CharField(max_length=100, null=True, blank=True)
  displayed_name = models.CharField(max_length=100, null=True, blank=True)
  
  address_line_1 = models.CharField(max_length=200, null=True, blank=True)
  address_line_2 = models.CharField(max_length=200, null=True, blank=True)
  zip_code = models.IntegerField(null=True, blank=True)
  country = models.CharField(max_length=200, null=True)
  website = models.URLField(null=True, blank=True)
  wikipedia_article = models.URLField(null=True, blank=True)

  @classmethod
  def create(cls, name, longitude, latitude, altitude, east_positive=True):
    site = cls(name=name)
    coords = TerrestrialCoordinates.create(longitude, latitude, altitude, east_positive)
    site.coordinates = coords
    site.displayed_name = site.name
    return site


class ObservingSite(Site):
  class Meta:
    app_label = 'iobserve'

  IAUCode = models.CharField(max_length=200, null=True, blank=True)



class ObservingPoint(EarthLocation):
  class Meta:
    app_label = 'iobserve'

  # site = models.ForeignKey('ObservingSite', related_name="sites")




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

  organisation_type = models.CharField(max_length=100, choices=ORGANISATION_TYPES_CHOICES, default=ORGANISATION_TYPE_UNKNOWN)

