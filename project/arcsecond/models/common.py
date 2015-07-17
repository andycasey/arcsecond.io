from django.db import models
from django.core.validators import RegexValidator
from constants import *

class Person(models.Model):
    class Meta: app_label = 'arcsecond'

    first_name = models.CharField(max_length=1000, default="")
    middle_name = models.CharField(max_length=1000, default="")
    last_name = models.CharField(max_length=1000, default="")


class BibliographicReference(models.Model):
    class Meta: app_label = 'arcsecond'

    title = models.CharField(max_length=1000, default="")
    year = models.IntegerField(default=0)
    bibcode = models.CharField(max_length=50, default="", validators=[RegexValidator(regex=bibcode_regex, message='Invalid bibcode', code='nomatch')])
    authors = models.ManyToManyField(Person, related_name="authors")


class Messages(models.Model):
    class Meta: app_label = 'arcsecond'

    warn = models.CharField(max_length=1000, default="")
    error = models.CharField(max_length=1000, default="")
    info = models.CharField(max_length=1000, default="")
    debug = models.CharField(max_length=1000, default="")
    http_status_code = models.IntegerField(default=0)

    def __init__(self, warn="", error="", info="", debug="", http_status_code=0):
        super(Messages, self).__init__(self)
        self.warn = warn
        self.error = error
        self.info = info
        self.debug = debug
        self.http_status_code = http_status_code
