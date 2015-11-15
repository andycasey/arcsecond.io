
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
        fields = ("bibcode", "eprint_id", "title", "year", "publication_type", "publication_date", "journal",
                  "abstract_copyright", "volume_number", "issue_number", "first_page_number", "number_of_pages",
                  "abstract", "subjects", "keywords", "is_refereed", "doi",
                  "authors", "references", "citations")

    journal = PublisherSerializer(required=False)
    doi = LinkSerializer(required=False)

    authors = PersonSerializer(required=False, many=True)
    references = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    citations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    publication_type = serializers.SerializerMethodField()
    def get_publication_type(self, obj):
        return Publication.PUBLICATION_TYPE_VALUES[Publication.PUBLICATION_TYPE_KEYS.index(obj.publication_type)]



