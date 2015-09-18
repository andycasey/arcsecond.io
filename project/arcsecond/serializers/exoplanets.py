from rest_framework import serializers

from project.arcsecond.models import Exoplanet

from .infos import *
from .coordinates import *
from .astronomicalobjects import *

######################## Exoplanets ########################

class ExoplanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exoplanet
        fields = ('name', 'coordinates', 'mass', 'radius', 'inclination', 'semi_major_axis', 'orbital_period',
                  'eccentricity', 'omega_angle', 'anomaly_angle', 'lambda_angle', 'time_periastron', 'time_conjonction',
                  'angular_distance', 'primary_transit', 'secondary_transit', 'impact_parameter', 'time_radial_velocity_zero',
                  'velocity_semiamplitude', 'calculated_temperature', 'measured_temperature', 'hottest_point_longitude',
                  'geometric_albedo', 'surface_gravity', 'detection_method', 'mass_detection_method', 'radius_detection_method',
                  'parent_star')

    coordinates = AstronomicalCoordinatesSerializer(required=False)
    parent_star = serializers.HyperlinkedIdentityField(view_name='astronomicalobject-detail',
                                                       lookup_field='parent_star_name',
                                                       lookup_url_kwarg='name',
                                                       read_only=True,
                                                       required=False)

    mass = MassSerializer(required=False)
    radius = RadiusSerializer(required=False)
    inclination = AngleSerializer(required=False)

    semi_major_axis = EllipseAxisSerializer(required=False)
    orbital_period = PeriodSerializer(required=False)
    eccentricity = EccentricitySerializer(required=False)

    omega_angle = AngleSerializer(required=False)
    anomaly_angle = AngleSerializer(required=False)
    lambda_angle = AngleSerializer(required=False)

    time_periastron = JulianDaySerializer(required=False)
    time_conjonction = JulianDaySerializer(required=False)
    angular_distance = AngleSerializer(required=False)

    primary_transit = JulianDaySerializer(required=False)
    secondary_transit = JulianDaySerializer(required=False)
    impact_parameter = AngleSerializer(required=False)
    time_radial_velocity_zero = JulianDaySerializer(required=False)
    velocity_semiamplitude = VelocitySerializer(required=False)

    calculated_temperature = TemperatureSerializer(required=False)
    measured_temperature = TemperatureSerializer(required=False)
    hottest_point_longitude = AngleSerializer(required=False)
    geometric_albedo = AlbedoSerializer(required=False)
    surface_gravity = GravitySerializer(required=False)

    detection_method = serializers.SerializerMethodField()
    mass_detection_method = serializers.SerializerMethodField()
    radius_detection_method = serializers.SerializerMethodField()

    def get_detection_method(self, obj):
        return Exoplanet.DETECTION_METHOD_VALUES[Exoplanet.DETECTION_METHOD_KEYS.index(obj.detection_method)]

    def get_mass_detection_method(self, obj):
        return Exoplanet.DETECTION_METHOD_VALUES[Exoplanet.DETECTION_METHOD_KEYS.index(obj.detection_method)]

    def get_radius_detection_method(self, obj):
        return Exoplanet.DETECTION_METHOD_VALUES[Exoplanet.DETECTION_METHOD_KEYS.index(obj.detection_method)]

