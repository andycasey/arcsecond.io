
from rest_framework import serializers
from project.arcsecond.models import Coordinates, ObservingSite, ObservingSiteActivity
from project.arcsecond.serializers import accounts


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('longitude', 'latitude', 'height')

class ObservingSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservingSite
        lookup_field = "name"
        fields = ('id', 'short_name', 'name', 'alternate_name_1', 'alternate_name_2', 'IAUCode', 'continent',
                  'coordinates', 'address_line_1', 'address_line_2', 'zip_code', 'country', 'state_province',
                  'time_zone', 'time_zone_name', 'telescopes', 'homepage', 'wikipedia_article', 'sources')

    coordinates = CoordinatesSerializer(required=False)
    telescopes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        coordinates_data = validated_data.pop('coordinates')
        site = ObservingSite.objects.create(**validated_data)
        if coordinates_data is not None:
            site.coordinates = Coordinates.objects.create(**coordinates_data)
            site.save()
        return site

    def update(self, instance, validated_data):
        coordinates_data = validated_data.pop('coordinates', None)
        coordinates = instance.coordinates

        excluded_fields = ["id", "coordinates", "telescopes"]
        filtered_fields = [f for f in self.fields if f not in excluded_fields]
        for field in filtered_fields:
            new_value = validated_data.get(field, getattr(instance, field))
            setattr(instance, field, new_value)

        if coordinates is None and coordinates_data is not None:
            instance.coordinates = Coordinates.objects.create(**coordinates_data)

        instance.save()
        return instance


class ObservingSiteShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservingSite
        lookup_field = "name"
        fields = ('id', 'short_name', 'name')

class ObservingSiteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservingSiteActivity
        fields = ('date', 'user', 'observing_site', 'action', 'property_name', 'old_value', 'new_value',
                  'action_message', 'method')

    user = accounts.UserSerializer(required=False)
    observing_site = ObservingSiteShortSerializer(required=False)

    action = serializers.SerializerMethodField()
    method = serializers.SerializerMethodField()

    def get_action(self, obj):
        return ObservingSiteActivity.ACTION_VALUES[ObservingSiteActivity.ACTION_KEYS.index(obj.action)]

    def get_method(self, obj):
        return ObservingSiteActivity.METHOD_VALUES[ObservingSiteActivity.METHOD_KEYS.index(obj.method)]