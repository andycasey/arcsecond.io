from django.contrib import auth
from rest_framework import serializers
from project.arcsecond.models import Link, Person, Publication

######################## Common ########################

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('title', 'url')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        lookup_field = 'bibcode'
        fields = ("bibcode", "eprint_id", "title", "year", "publication_type", "publication_date", "journal_name",
                  "abstract_copyright", "volume_number", "issue_number", "first_page_number", "number_of_pages",
                  "abstract", "subjects", "keywords", "origin", "is_refereed", "bibtex_entry", "doi", "authors")

    doi = LinkSerializer(required=False)
    authors = PersonSerializer(required=False, many=True)

    publication_type = serializers.SerializerMethodField()
    def get_publication_type(self, obj):
        return Publication.PUBLICATION_VALUES[Publication.PUBLICATION_KEYS.index(obj.publication_type)]



