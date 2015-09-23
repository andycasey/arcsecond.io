from rest_framework import serializers
from project.arcsecond.models import ESOProgrammeSummary, HSTProgrammeSummary, ESOArchiveDataRow

######################## Archives ########################

class ESOProgrammeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ESOProgrammeSummary
        lookup_field = "programme_id"

class ESOArchiveDataRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESOArchiveDataRow

class HSTProgrammeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HSTProgrammeSummary
        lookup_field = "programme_id"
