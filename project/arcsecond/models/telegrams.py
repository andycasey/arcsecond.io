from django.db import models
from .common import Link, Person
from .sky import AstronomicalObject

class AstronomersTelegram(models.Model):
    class Meta: app_label = 'arcsecond'

    identifier = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    credential_certification = models.CharField(max_length=500, null=True, blank=True)
    subjects = models.CharField(max_length=200, null=True, blank=True)
    content = models.CharField(max_length=20000, null=True, blank=True)

    related_telegrams = models.ManyToManyField('self')

    authors = models.ManyToManyField(Person, related_name='astronomer_telegrams')
    external_links = models.ManyToManyField(Link, related_name='astronomer_telegrams')
    detected_objects = models.ManyToManyField(AstronomicalObject, related_name='astronomer_telegrams')


class GCNCircular(models.Model):
    class Meta: app_label = 'arcsecond'

    identifier = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    content = models.CharField(max_length=20000, null=True, blank=True)
    submitter = models.ForeignKey(Person, null=True, blank=True, related_name='submitted_GCN_circulars')

    related_circulars = models.ManyToManyField('self')

    authors = models.ManyToManyField(Person, related_name='GCN_circulars')
    external_links = models.ManyToManyField(Link, related_name='GCN_circulars')
    detected_objects = models.ManyToManyField(AstronomicalObject, related_name='GCN_circulars')




