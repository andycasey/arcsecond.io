from rest_framework import serializers
from project.arcsecond.models.archives import *
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
    telescope = TelescopeSerializer(required=False)

class HSTProgrammeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HSTProgrammeSummary
        lookup_field = "programme_id"
