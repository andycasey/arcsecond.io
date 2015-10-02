from rest_framework import serializers
from project.arcsecond.models import AstronomicalObject, Alias, ObjectType

from .telegrams import *
from .coordinates import *
from .infos import *


######################## Objects Properties ########################


class AliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ("name", "catalogue_url")

class ObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectType
        fields = ("value",)



######################## Objects ########################

class AstronomicalObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomicalObject
        lookup_field = "name"
        fields = ('name', 'coordinates', 'aliases', 'object_types', 'fluxes', 'mass', 'radius', 'distance',
                  'metallicity', 'age', 'effective_temperature', 'planets', 'astronomer_telegrams', 'finding_charts')

    coordinates = AstronomicalCoordinatesSerializer(required=False)

    aliases = AliasSerializer(many=True, required=False)
    object_types = ObjectTypeSerializer(many=True, required=False)
    fluxes = FluxSerializer(many=True, required=False)

    mass = MassSerializer(required=False)
    radius = RadiusSerializer(required=False)
    distance = DistanceSerializer(required=False)
    metallicity = MetallicitySerializer(required=False)
    age = AgeSerializer(required=False)
    effective_temperature = TemperatureSerializer(required=False)

    planets = serializers.HyperlinkedRelatedField(view_name='exoplanet-named-detail',
                                                  lookup_field='name',
                                                  many=True,
                                                  read_only=True,
                                                  required=False)

    astronomer_telegrams = serializers.HyperlinkedRelatedField(view_name='astronomerstelegram-detail',
                                                               lookup_field='name',
                                                               lookup_url_kwarg='identifier',
                                                               many=True,
                                                               read_only=True,
                                                               required=False)

    finding_charts = serializers.HyperlinkedIdentityField(view_name='findingchart-list',
                                                          lookup_field='name',
                                                          lookup_url_kwarg='input',
                                                          read_only=True,
                                                          required=False)




