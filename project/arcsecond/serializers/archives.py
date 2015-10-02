from rest_framework import serializers
from project.arcsecond.models.archives import *
from project.arcsecond.serializers.coordinates import AstronomicalCoordinatesSerializer
from project.arcsecond.serializers.telescopes import *

######################## Archives ########################

class ESOProgrammeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ESOProgrammeSummary
        lookup_field = "programme_id"

class DataArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataArchive
        fields = ('name', 'url')

class ESOArchiveDataRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESOArchiveDataRow

    archive = DataArchiveSerializer(required=False)
    summary = ESOProgrammeSummarySerializer(required=False)
    coordinates = AstronomicalCoordinatesSerializer(required=False)
    telescope = serializers.HyperlinkedRelatedField(view_name='telescope-detail',
                                                    lookup_field='name',
                                                    read_only=True,
                                                    required=False)

class HSTProgrammeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HSTProgrammeSummary
        lookup_field = "programme_id"
