from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField, DateRangeField
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .constants import *
from .sky import AstronomicalObject

class Error(models.Model):
    class Meta: app_label = 'arcsecond'
    code = models.PositiveSmallIntegerField()
    message = models.CharField(max_length=1000, null=True, blank=True)

class Link(models.Model):
    class Meta: app_label = 'arcsecond'
    title = models.CharField(max_length=1000, null=True, blank=True)
    url = models.URLField(max_length=2000, null=True, blank=True)
    publications = models.ForeignKey('Publication', null=True, blank=True, related_name='download_links')

# See https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/fields/#contains
class PersonManager(models.Manager):
    def get_flexibly_or_create(self, **kwargs):
        created = False
        last_name = kwargs.get('last_name', "").strip()
        initials = kwargs.get('initials', [])
        first_name = kwargs.get('first_name', "").strip()
        person = None
        try:
            person = Person.objects.get(last_name=last_name, first_name=first_name, initials__overlap=initials)
        except ObjectDoesNotExist:
            try:
                # Try without initials
                person = Person.objects.get(last_name=last_name, first_name=first_name)
            except ObjectDoesNotExist:
                # Play with initials if we have some. Else, use first_name
                if len(initials) > 0:
                    try:
                        person = Person.objects.get(last_name=last_name, first_name__startswith=initials[0].replace('.', '').strip())
                    except ObjectDoesNotExist:
                        try:
                            person = Person.objects.get(last_name=last_name)
                        except ObjectDoesNotExist:
                            pass
                        except MultipleObjectsReturned:
                            print 'MultipleObjectsReturned returned for person lookup:', last_name
                elif len(first_name) > 1:
                    try:
                        person = Person.objects.get(last_name=last_name, initials__overlap=[first_name[0]+'.'])
                    except ObjectDoesNotExist:
                        pass
                    except MultipleObjectsReturned:
                        print 'MultipleObjectsReturned returned for person lookup:', last_name, first_name

        except MultipleObjectsReturned:
            # Filter and pick first.
            person = Person.objects.filter(last_name=last_name, first_name=first_name, initials__overlap=initials).first()
            print 'MultipleObjectsReturned returned for person lookup:', kwargs

        if person is None:
            person = Person.objects.create(last_name=last_name, first_name=first_name, initials=initials)
            created = True

        return person, created


class Person(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = PersonManager()
    first_name = models.CharField(max_length=1000, null=True, blank=True)
    middle_name = models.CharField(max_length=1000, null=True, blank=True)
    last_name = models.CharField(max_length=1000, null=True, blank=True)
    initials = ArrayField(models.CharField(max_length=10, null=True, blank=True), default=list)

    def __unicode__(self):
        s = u""
        s += self.first_name
        if len(self.initials) > 0:
            s += u', '.join(self.initials)
        s += self.last_name
        return s

class Organisation(models.Model):
    class Meta: app_label = 'arcsecond'
    name = models.CharField(max_length=1000, null=True, blank=True)


class PublisherManager(models.Manager):
    def get_flexibly_or_create(self, **kwargs):
        name = kwargs.get('name', None)
        acronym = kwargs.get('acronym', None)
        created = False

        if name is not None and acronym is None:
            return Publisher.objects.get_or_create(name=name)

        elif name is None and acronym is not None:
            return Publisher.objects.get_or_create(acronym=acronym)

        elif name is not None and acronym is not None:
            try:
                publisher = Publisher.objects.get(name=name)
            except ObjectDoesNotExist:
                try:
                    publisher = Publisher.objects.get(acronym=acronym)
                except ObjectDoesNotExist:
                    publisher = Publisher.objects.create(name=name, acronym=acronym)
                    created = True

            return publisher, created

        else:
            return None, False


class Publisher(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = PublisherManager()
    name = models.CharField(max_length=1000, null=True, blank=True)
    acronym = models.CharField(max_length=20, null=True, blank=True)

class Affiliation(models.Model):
    class Meta: app_label = 'arcsecond'
    person = models.ForeignKey(Person, null=True, blank=True, related_name="affiliations")
    organisation = models.ForeignKey(Organisation, null=True, blank=True, related_name="affiliations")
    dates = DateRangeField(null=True, blank=True)

class Publication(models.Model):
    class Meta: app_label = 'arcsecond'

    PUBLICATION_TYPE_UNKNOWN = "unk"
    PUBLICATION_TYPE_ARTICLE = "art"
    PUBLICATION_TYPE_PROCEEDINGS = "proc"
    PUBLICATION_TYPE_PROPOSAL = "prop"
    PUBLICATION_TYPE_PREPRINT = "prep"

    PUBLICATION_TYPE_KEYS = (PUBLICATION_TYPE_UNKNOWN, PUBLICATION_TYPE_ARTICLE, PUBLICATION_TYPE_PROCEEDINGS, PUBLICATION_TYPE_PROPOSAL, PUBLICATION_TYPE_PREPRINT)
    PUBLICATION_TYPE_VALUES = ('unknown', 'article', 'proceedings', 'proposal', 'preprint')
    PUBLICATION_TYPE_CHOICES = tuple(zip(PUBLICATION_TYPE_KEYS, PUBLICATION_TYPE_VALUES))

    publication_type = models.CharField(max_length=5, choices=PUBLICATION_TYPE_CHOICES, default=PUBLICATION_TYPE_UNKNOWN)
    publication_date = models.DateField(null=True, blank=True)

    abstract = models.CharField(max_length=5000, null=True, blank=True)
    abstract_copyright = models.CharField(max_length=200, null=True, blank=True)

    authors = models.ManyToManyField(Person, related_name="publications")

    bibcode = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=bibcode_regex, message='Invalid bibcode', code='nomatch')])
    eprint_id = models.CharField(max_length=50, null=True, blank=True)
    doi = models.OneToOneField(Link, null=True, blank=True, related_name='doi')

    citations = models.ManyToManyField('self', related_name="citations")
    references = models.ManyToManyField('self', related_name="references")

    keywords = ArrayField(models.CharField(max_length=100, null=True, blank=True), default=list)
    subjects = ArrayField(models.CharField(max_length=200, null=True, blank=True), default=list)

    journal = models.ForeignKey(Publisher, null=True, blank=True, related_name='publications')
    volume_number = models.IntegerField(null=True, blank=True)
    issue_number = models.IntegerField(null=True, blank=True)
    first_page_number = models.IntegerField(null=True, blank=True)
    number_of_pages = models.IntegerField(null=True, blank=True)
    is_refereed = models.BooleanField(default=False, blank=True)

    title = models.CharField(max_length=1000, default="", null=True, blank=True)
    year = models.IntegerField(default=0, null=True, blank=True)

    related_objects = models.ManyToManyField(AstronomicalObject, related_name="related_objects")



