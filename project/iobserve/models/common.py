from django.db import models

class Person(models.Model):
    class Meta: app_label = 'iobserve'

    first_name = models.CharField(max_length=1000)
    middle_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)


class BibliographicReference(models.Model):
    class Meta: app_label = 'iobserve'

    title = models.CharField(max_length=1000)
    year = models.IntegerField(default=0)

# bibcode = models.RegexField(regex="[0-9]{4}[A-Za-z].{12}[0-9][A-Z]")
#  authors = models.ManyToManyField(Person, related_name="authors")

