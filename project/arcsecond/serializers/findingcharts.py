from rest_framework import serializers
from project.arcsecond.models import FindingChart, AstronomicalObject

######################## Finding Charts ########################

class FindingChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindingChart
        lookup_field = "pk"
        fields = ('input', 'astronomical_object', 'survey_name', 'width', 'height', 'size_unit', 'orientation',
                  'band_name', 'observing_date', 'fits_url', 'image_url')

    astronomical_object = serializers.HyperlinkedRelatedField(view_name='astronomicalobject-detail', lookup_field='name', read_only=True)
    survey_name = serializers.SerializerMethodField()
    size_unit = serializers.SerializerMethodField()
    orientation = serializers.SerializerMethodField()

    def get_survey_name(self, obj):
        return FindingChart.SURVEY_NAME_VALUES[FindingChart.SURVEY_NAME_KEYS.index(obj.survey_name)]

    def get_size_unit(self, obj):
        return FindingChart.SIZE_UNIT_VALUES[FindingChart.SIZE_UNIT_KEYS.index(obj.size_unit)]

    def get_orientation(self, obj):
        return FindingChart.ORIENTATION_VALUES[FindingChart.ORIENTATION_KEYS.index(obj.orientation)]
