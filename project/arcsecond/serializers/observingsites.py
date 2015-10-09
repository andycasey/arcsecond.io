from django.contrib import auth
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
                  'coordinates', 'address_line_1', 'address_line_2', 'zip_code', 'country',
                  'time_zone', 'time_zone_name', 'telescopes')

    coordinates = CoordinatesSerializer()
    telescopes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth.get_user_model()
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class ObservingSiteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservingSiteActivity
        fields = ('date', 'user', 'observing_site', 'action', 'property_name', 'old_value', 'new_value',
                  'action_message', 'method')

    user = UserSerializer(required=False)
    observing_site = ObservingSiteSerializer(required=False)

    action = serializers.SerializerMethodField()
    method = serializers.SerializerMethodField()

    def get_action(self, obj):
        return ObservingSiteActivity.ACTION_VALUES[ObservingSiteActivity.ACTION_KEYS.index(obj.action)]

    def get_method(self, obj):
        return ObservingSiteActivity.METHOD_VALUES[ObservingSiteActivity.METHOD_KEYS.index(obj.method)]