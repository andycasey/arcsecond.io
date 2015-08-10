from django.db import models
from .common import *

class AstronomersTelegram(models.Model):
    class Meta: app_label = 'arcsecond'

    identifier = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=20000, null=True, blank=True)
    related_telegrams = models.ManyToManyField('self')
    external_links = models.ManyToManyField(Link, related_name='astronomer_telegrams')



