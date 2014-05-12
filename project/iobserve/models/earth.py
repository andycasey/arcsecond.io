
from django.db import models
from constants import *
from common import *


class TerrestrialCoordinates(models.Model):
  class Meta:
    app_label = 'iobserve'
    unique_together = (('longitude', 'latitude'),)

  longitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  latitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  east_positive = models.BooleanField(default=True)
  altitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)

  def are_empty(self):
    return self.longitude == NOT_A_SCIENTIFIC_NUMBER or \
        self.latitude == NOT_A_SCIENTIFIC_NUMBER or \
        self.altitude == NOT_A_SCIENTIFIC_NUMBER
      
  def __unicode__(self):
    return u"(long: %.8f, lat: %.8f, alt: %.2fm)"%(self.longitude, self.latitude, self.altitude)
   
   
class TerrestrialObject(models.Model):
  class Meta:
    app_label = 'iobserve'
  
  name = models.CharField(max_length=100, primary_key=True)
  long_name = models.CharField(max_length=100)
  coordinates = TerrestrialCoordinates()

  CONTINENT_ASIA = "Asia"
  CONTINENT_ANTARCTICA = "Antarctica"
  CONTINENT_EUROPE = "Europe"
  CONTINENT_NORTH_AMERICA = "North America"
  CONTINENT_OCEANIA = "Oceania"
  CONTINENT_SOUTH_AMERICA = "South America"
  
  CONTINENTS_TYPES_CHOICES = (
    (CONTINENT_ASIA, 'Asia'),
    (CONTINENT_ANTARCTICA, 'Antarctica'),
    (CONTINENT_EUROPE, 'Europe'),
    (CONTINENT_NORTH_AMERICA, 'North America'),
    (CONTINENT_OCEANIA, 'Oceania'),
    (CONTINENT_SOUTH_AMERICA, 'South America'),
  )
  
  continent = models.CharField(max_length=100, choices=CONTINENTS_TYPES_CHOICES)

  def __unicode__(self):
    return "%s (%s, %s)"%(self, self.name, self.coordinates)


class ObservingTool(TerrestrialObject):
  class Meta:
    app_label = 'iobserve'

  TOOL_TYPE_TELESCOPE = "Telescope"
  TOOL_TYPE_ANTENNA = "Antenna"

  TOOL_TYPES_CHOICES = (
    (TOOL_TYPE_TELESCOPE, 'Telescope'),
    (TOOL_TYPE_ANTENNA, 'Antenna'),
  )

  tool_type = models.CharField(max_length=100, choices=TOOL_TYPES_CHOICES)
  site = models.ForeignKey('ObservingSite', related_name="sites")


class Site(TerrestrialObject):
  class Meta:
    app_label = 'iobserve'
    
  acronym = models.CharField(max_length=200)
  address_line_1 = models.CharField(max_length=200)
  address_line_2 = models.CharField(max_length=200)
  zip_code = models.IntegerField()
  country = models.CharField(max_length=200)
  website = models.URLField()
  wikipedia_article = models.URLField()


class ObservingSite(Site):
  class Meta:
    app_label = 'iobserve'

  IAUCode = models.CharField(max_length=200)


class AstronomicalOrganisation(models.Model):
  class Meta:
    app_label = 'iobserve'
    
  name = models.CharField(max_length=100, primary_key=True)
  acronym = models.CharField(max_length=100)

  headquarters = models.OneToOneField(Site, related_name="astronomical_organisation")
  observing_sites = models.ManyToManyField(ObservingSite, related_name="astronomical_organisations")

  website = models.URLField()
  wikipedia_article = models.URLField()

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

