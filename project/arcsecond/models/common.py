from django.db import models
from django.core.validators import RegexValidator

from .constants import *
from .sky import AstronomicalObject

class Link(models.Model):
    class Meta: app_label = 'arcsecond'

    title = models.CharField(max_length=1000, null=True, blank=True)
    url = models.URLField(max_length=2000, null=True, blank=True)

    publications = models.ForeignKey('Publication', null=True, blank=True, related_name='download_links')


class Person(models.Model):
    class Meta: app_label = 'arcsecond'

    first_name = models.CharField(max_length=1000, default="")
    middle_name = models.CharField(max_length=1000, default="")
    last_name = models.CharField(max_length=1000, default="")

    profile_URL = models.URLField(max_length=200, null=True, blank=True)


class Publication(models.Model):
    class Meta: app_label = 'arcsecond'

    title = models.CharField(max_length=1000, default="", null=True, blank=True)
    year = models.IntegerField(default=0, null=True, blank=True)

    bibcode = models.CharField(max_length=50, default="", validators=[RegexValidator(regex=bibcode_regex, message='Invalid bibcode', code='nomatch')])
    eprint_id = models.CharField(max_length=50, null=True, blank=True)

    PUBLICATION_UNKNOWN = "unk"
    PUBLICATION_ARTICLE = "art"
    PUBLICATION_PROCEEDINGS = "proc"

    PUBLICATION_KEYS = (PUBLICATION_UNKNOWN, PUBLICATION_ARTICLE, PUBLICATION_PROCEEDINGS)
    PUBLICATION_VALUES = ('unknown', 'article', 'proceedings')
    PUBLICATION_CHOICES = tuple(zip(PUBLICATION_KEYS, PUBLICATION_VALUES))

    publication_type = models.CharField(max_length=3, choices=PUBLICATION_CHOICES, default=PUBLICATION_UNKNOWN)
    publication_date = models.DateField(null=True, blank=True)

    journal_name = models.CharField(max_length=100, null=True, blank=True)
    abstract_copyright = models.CharField(max_length=200, null=True, blank=True)
    volume_number = models.IntegerField(null=True, blank=True)
    issue_number = models.IntegerField(null=True, blank=True)
    first_page_number = models.IntegerField(null=True, blank=True)
    number_of_pages = models.IntegerField(null=True, blank=True)

    abstract = models.CharField(max_length=5000, null=True, blank=True)
    subjects = models.CharField(max_length=200, null=True, blank=True)
    keywords = models.CharField(max_length=300, null=True, blank=True)

    origin = models.URLField(max_length=200, null=True, blank=True)
    is_refereed = models.BooleanField(default=True, blank=True)

    bibtex_entry = models.CharField(max_length=5000, null=True, blank=True)
    doi = models.OneToOneField(Link, null=True, blank=True, related_name='doi')

    authors = models.ManyToManyField(Person, related_name="publications")
    references = models.ManyToManyField('self', related_name="references")
    citations = models.ManyToManyField('self', related_name="citations")

    related_objects = models.ManyToManyField(AstronomicalObject, related_name="related_objects")


