from rest_framework import serializers
from project.arcsecond.models import AstronomersTelegram, GCNCircular
from .common import *

######################## Telegrams ########################

class AstronomersTelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomersTelegram
        lookup_field = "identifier"
        fields = ('identifier', 'title', 'credential_certification', 'subjects', 'content', 'authors',
                  'related_telegrams', 'detected_objects', 'external_links')

    related_telegrams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    detected_objects = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    subjects = serializers.SerializerMethodField()
    def get_subjects(self, obj):
        return [AstronomersTelegram.SUBJECTS_VALUES[AstronomersTelegram.SUBJECTS_KEYS.index(domain)] for domain in obj.subjects]

class GCNCircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCNCircular
        lookup_field = "identifier"
        fields = ('identifier', 'title', 'date', 'content', 'submitter', 'authors',
                  'related_circulars', 'external_links')

    submitter = PersonSerializer(required=False)
    related_circulars = serializers.HyperlinkedIdentityField(many=True,
                                                             read_only=True,
                                                             view_name='gcncircular-detail',
                                                             lookup_field='identifier')


