
from rest_framework import serializers
from project.arcsecond.models.common import *

######################## Common ########################

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('title', 'url')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "first_name", "middle_name", "initials", "last_name", "affiliations")

    affiliations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ("name", "acronym")


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        lookup_field = 'bibcode'
        fields = ("id", "bibcode", "eprint_id", "doi", "year", "month", "publication_date", "publication_type",
                  "title", "abstract", "subjects", "keywords", "is_refereed", "authors",
                  "journal", "volume_number", "issue_number", "first_page_number", "number_of_pages",
                  "references", "citations")

    journal = PublisherSerializer(required=False)
    doi = LinkSerializer(required=False)

    authors = PersonSerializer(required=False, many=True)
    references = serializers.SlugRelatedField(slug_field='bibcode',
                                             many=True,
                                             read_only=True,
                                             required=False)
    citations = serializers.SlugRelatedField(slug_field='bibcode',
                                             many=True,
                                             read_only=True,
                                             required=False)

    publication_type = serializers.SerializerMethodField()
    def get_publication_type(self, obj):
        return Publication.PUBLICATION_TYPE_VALUES[Publication.PUBLICATION_TYPE_KEYS.index(obj.publication_type)]



