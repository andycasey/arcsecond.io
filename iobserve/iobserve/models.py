from django.db import models

NOT_A_SCIENTIFIC_NUMBER = -9999999999999

class Coordinates(models.Model):
  """
  The generic coordinates class
  """

  COORDINATES_SPHERICAL = "Spherical"
  COORDINATES_ASTRO = "Astro"
  COORDINATES_TERRESTRIAL = "Terrestrial"

  COORDINATES_TYPES_CHOICES = (
    (COORDINATES_SPHERICAL, 'Spherical Coordinates'),
    (COORDINATES_ASTRO, 'Astronomical Coordinates'),
    (COORDINATES_TERRESTRIAL, 'Terrestrial Coordinates'),
  )
  
  coords_type = models.CharField(max_length=30, choices=COORDINATES_TYPES_CHOICES, default=COORDINATES_SPHERICAL)
  
  theta = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  phi = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  
  def are_empty(self):
    return self.theta == NOT_A_SCIENTIFIC_NUMBER and self.phi == NOT_A_SCIENTIFIC_NUMBER
  
  def __unicode__(self):
    return "%s (%.8f, %.8f)"%(self.coords_type, self.theta, self.phi)
    
    
class ModelObject(models.Model):
  name = models.CharField(max_length=100)
  long_name = models.CharField(max_length=100)
  coordinates = Coordinates()
  
  def __unicode__(self):
    return "%s (%s)"%(self, self.name)

class ObservingTool(ModelObject):
  pass
  
class Observatory(ModelObject):
  pass
  
class AstronomicalOrganisation(models.Model):
  pass