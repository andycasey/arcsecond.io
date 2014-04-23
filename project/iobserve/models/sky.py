
from django.db import models
from constants import *
from common import *

class AstronomicalCoordinates(models.Model):
  class Meta:
    app_label = 'iobserve'
  
  right_ascension = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  declination = models.FloatField(default=NOT_A_SCIENTIFIC_NUMBER)
  epoch = models.FloatField(default=J2000)
  equinox = models.FloatField(default=J2000)
  source = models.CharField(max_length=1000, blank=True)
#  reference = models.OneToOneField(BibliographicReference, blank=True)

  def are_empty(self):
    return self.right_ascension == NOT_A_SCIENTIFIC_NUMBER or \
      self.declination == NOT_A_SCIENTIFIC_NUMBER or \
      self.epoch == NOT_A_SCIENTIFIC_NUMBER

  def __unicode__(self):
    return u"(R.A.: %.8f, Dec: %.8f, epoch: %.2f, equinox: %.2f)"%(self.right_ascension, self.declination, self.epoch, self.equinox)


class Alias(models.Model):
  class Meta:
    app_label = 'iobserve'

  value = models.CharField(max_length=100)


class AstronomicalObject(models.Model):
  class Meta:
    app_label = 'iobserve'

  name = models.CharField(max_length=100)
  coordinates = models.OneToOneField(AstronomicalCoordinates, blank=True)
#  references = models.ManyToManyField(BibliographicReference, related_name="references", blank=True)
  aliases = models.ManyToManyField(Alias, related_name="aliases", blank=True)



