from django.db import models

NOT_A_SCIENTIFIC_NUMBER = -9999999999999
J2000 = 2000

class AstronomicalCoordinates(models.Model):
  right_ascension = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  declination = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  epoch = models.FloatField(default=J2000)
  equinox = models.FloatField(default=J2000)

  def are_empty(self):
    return self.right_ascension == NOT_A_SCIENTIFIC_NUMBER or \
      self.declination == NOT_A_SCIENTIFIC_NUMBER or \
      self.epoch == NOT_A_SCIENTIFIC_NUMBER

  def __unicode__(self):
    return u"(R.A.: %.8f, Dec: %.8f, epoch: %.2f, equinox: %.2f)"%(self.right_ascension, self.declination, self.epoch)

class BibliographicReference(models.Model):
  title = models.CharField(max_length=1000)

class Alias(models.Model):
  value = models.CharField(max_length=100)
  catalogue_name = models.CharField(max_length=100)
  astronomical_object = models.ForeignKey('AstronomicalObject', related_name='alias')

class AstronomicalObject(models.Model):
  name = models.CharField(max_length=100)
  coordinates = AstronomicalCoordinates()
  #references = models.ManyToManyField(BibliographicReference, related_name="references")

class TerrestrialCoordinates(models.Model):
  longitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  latitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  east_positive = models.BooleanField()
  altitude = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  
  def are_empty(self):
    return self.longitude == NOT_A_SCIENTIFIC_NUMBER or \
        self.latitude == NOT_A_SCIENTIFIC_NUMBER or \
        self.altitude == NOT_A_SCIENTIFIC_NUMBER
  
  def __unicode__(self):
    return u"(long: %.8f, lat: %.8f, alt: %.2fm)"%(self.longitude, self.latitude, self.altitude)
        
class TerrestrialObject(models.Model):
  name = models.CharField(max_length=100)
  long_name = models.CharField(max_length=100)
  coordinates = TerrestrialCoordinates()
  
  def __unicode__(self):
    return "%s (%s, %s)"%(self, self.name, self.coordinates)

class ObservingTool(TerrestrialObject):
  TOOL_TYPE_DOME = "Dome"
  TOOL_TYPE_ANTENNA = "Antenna"
  
  TOOL_TYPES_CHOICES = (
    (TOOL_TYPE_DOME, 'Dome'),
    (TOOL_TYPE_ANTENNA, 'Antenna'),
  )
  
  tool_type = models.CharField(max_length=100, choices=TOOL_TYPES_CHOICES)

  
class Site(TerrestrialObject):
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

  TYPE_UNKNOWN = 'Unknown'
  TYPE_PUBLIC = 'Public Site'
  TYPE_MIXED = 'Mixed Public/Private Site'
  TYPE_PRIVATE = 'Private Site'
  
  TYPES_CHOICES = (
    (TYPE_UNKNOWN, 'Unknown'),
    (TYPE_PUBLIC, 'Public Site'),
    (TYPE_MIXED, 'Mixed Public/Private Site'),
    (TYPE_PRIVATE, 'Private Site'),
  )
  
  site_type = models.CharField(max_length=100, choices=TYPES_CHOICES, default=TYPE_UNKNOWN)
  
  acronym = models.CharField(max_length=200)
  address_line_1 = models.CharField(max_length=200)
  address_line_2 = models.CharField(max_length=200)
  zip_code = models.IntegerField()
  country = models.CharField(max_length=200)
  website = models.URLField()
    
class ObservingSite(Site):
  pass
  
class AstronomicalOrganisation(models.Model):
  headquarters = models.OneToOneField(Site, related_name="headquarters")
  secondary_headquarters = models.OneToOneField(Site, related_name="secondary_headquarters")
  observing_sites = models.ManyToManyField(ObservingSite, related_name="observing_sites")
  
  
  