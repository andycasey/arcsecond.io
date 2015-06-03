from django.db import models
from django.core.validators import RegexValidator

bibcode_regex = "^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$"

class Person(models.Model):
    class Meta: app_label = 'iobserve'

    first_name = models.CharField(max_length=1000, default="")
    middle_name = models.CharField(max_length=1000, default="")
    last_name = models.CharField(max_length=1000, default="")


class BibliographicReference(models.Model):
    class Meta: app_label = 'iobserve'

    title = models.CharField(max_length=1000, default="")
    year = models.IntegerField(default=0)
    bibcode = models.CharField(max_length=18, default="", validators=[RegexValidator(regex=bibcode_regex, message='Invalid bibcode', code='nomatch')])
    authors = models.ManyToManyField(Person, related_name="authors")

