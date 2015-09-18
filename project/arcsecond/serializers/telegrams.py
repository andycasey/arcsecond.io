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

    related_telegrams = serializers.HyperlinkedRelatedField(many=True,
                                                            read_only=True,
                                                            view_name='astronomerstelegram-detail',
                                                            lookup_field='identifier')

    detected_objects = serializers.HyperlinkedRelatedField(many=True,
                                                           read_only=True,
                                                           view_name='astronomicalobject-detail',
                                                           lookup_field='name')


class GCNCircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCNCircular
        lookup_field = "identifier"
        fields = ('identifier', 'title', 'date', 'content', 'submitter', 'authors',
                  'related_circulars', 'external_links')

    submitter = PersonSerializer(required=False)
    related_circulars = serializers.HyperlinkedRelatedField(many=True,
                                                            read_only=True,
                                                            view_name='gcncircular-detail',
                                                            lookup_field='identifier')


