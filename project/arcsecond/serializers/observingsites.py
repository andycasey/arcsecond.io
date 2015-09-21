from rest_framework import serializers
from project.arcsecond.models import Coordinates, ObservingSite, ObservingSiteActivity

######################## Earth ########################

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('longitude', 'latitude', 'height')

######################## Observing Sites ########################


class ObservingSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservingSite
        lookup_field = "name"
        fields = ('id', 'short_name', 'name', 'alternate_name_1', 'alternate_name_2', 'IAUCode', 'continent',
                  'coordinates', 'address_line_1', 'address_line_2', 'zip_code', 'country', 'time_zone', 'time_zone_name',
                  'telescopes')

    coordinates = CoordinatesSerializer()
    telescopes = serializers.HyperlinkedRelatedField(many=True,
                                                     read_only=True,
                                                     view_name='telescope-detail',
                                                     lookup_field='name')

class ObservingSiteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservingSiteActivity