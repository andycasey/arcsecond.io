
from rest_framework import serializers
from .models import *

######################## Shorts ########################

class AstronomicalObjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomicalObject
        lookup_field = "name"
        fields = ('url', 'name')

class AstronomersTelegramShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomersTelegram
        lookup_field = "identifier"
        fields = ('url', 'identifier')

class PublicationShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        lookup_field = "bibcode"
        fields = ('url', 'bibcode')


######################## Common ########################

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('title', 'url')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        lookup_field = 'bibcode'
        fields = ("url", "bibcode", "eprint_id", "title", "year", "publication_type", "publication_date", "journal_name",
                  "abstract_copyright", "volume_number", "issue_number", "first_page_number", "number_of_pages",
                  "abstract", "subjects", "keywords", "origin", "is_refereed", "bibtex_entry", "doi", "authors",
                  # "references",
                  # "citations",
                  # "related_objects"
                  )

    doi = LinkSerializer(required=False)

    authors = PersonSerializer(required=False, many=True)
    # references = PublicationShortSerializer(required=False, many=True)
    # references = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='publication-detail',
    #     lookup_field='bibcode'
    # )

    # citations = PublicationShortSerializer(required=False, many=True)
    # related_objects = AstronomicalObjectShortSerializer(required=False, many=True)

    publication_type = serializers.SerializerMethodField()
    def get_publication_type(self, obj):
        return Publication.PUBLICATION_VALUES[Publication.PUBLICATION_KEYS.index(obj.publication_type)]


######################## Infos ########################


class JulianDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = JulianDay
        fields = ("value", "error_max", "error_min", "bibcode")

class AlbedoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albedo
        fields = ("value", "error_max", "error_min", "bibcode")

class EccentricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Eccentricity
        fields = ("value", "error_max", "error_min", "bibcode")

class FluxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flux
        fields = ("name", "value", "error_max", "error_min", "bibcode")

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("first_magnitude_name", "second_magnitude_name", "value", "error", "bibcode")

class MassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mass
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Mass.MASSES_VALUES[Mass.MASSES_KEYS.index(obj.unit)]

class RadiusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radius
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Radius.RADIUS_VALUES[Radius.RADIUS_KEYS.index(obj.unit)]

class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Age.AGE_VALUES[Age.AGE_KEYS.index(obj.unit)]


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Temperature.TEMP_VALUES[Temperature.TEMP_KEYS.index(obj.unit)]


class MetallicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Metallicity
        fields = ("value", "unit", "error", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Metallicity.METAL_VALUES[Metallicity.METAL_KEYS.index(obj.unit)]


class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Distance.DISTANCE_VALUES[Distance.DISTANCE_KEYS.index(obj.unit)]


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Period.PERIOD_VALUES[Period.PERIOD_KEYS.index(obj.unit)]


class EllipseAxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = EllipseAxis
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return EllipseAxis.AXIS_VALUES[EllipseAxis.AXIS_KEYS.index(obj.unit)]

class AngleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angle
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

    unit = serializers.SerializerMethodField()
    def get_unit(self, obj):
        return Angle.ANGLE_VALUES[Angle.ANGLE_KEYS.index(obj.unit)]

class VelocitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")

class GravitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields = ("value", "unit", "error_max", "error_min", "bibcode")



######################## Earth ########################

class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('longitude', 'latitude', 'height')

class ObservingSiteSerializer(serializers.HyperlinkedModelSerializer):
    coordinates = CoordinatesSerializer()

    class Meta:
        model = ObservingSite
        lookup_field = "name"
        fields = ('name', 'long_name', 'IAUCode', 'continent', 'coordinates', 'address_line_1', 'address_line_2',
                  'zip_code', 'country', 'time_zone', 'time_zone_name')


######################## Objects Properties ########################

class AstronomicalCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomicalCoordinates
        fields = ("system", "right_ascension", "right_ascension_units", "declination", "declination_units", "epoch", "equinox")

class AliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = ("name", "catalogue_url")

class ObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectType
        fields = ("value",)



######################## Objects ########################

class AstronomicalObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AstronomicalObject
        lookup_field = "name"
        fields = ('url', 'name', 'coordinates', 'aliases', 'object_types', 'fluxes', 'mass', 'radius', 'distance',
                  'metallicity', 'age', 'effective_temperature', 'astronomer_telegrams')

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

    astronomer_telegrams = AstronomersTelegramShortSerializer(required=False, many=True)


######################## Exoplanets ########################

class ExoplanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exoplanet

    coordinates = AstronomicalCoordinatesSerializer(required=False)
    parent_star = AstronomicalObjectSerializer()

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



######################## Archives ########################

class ESOProgrammeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ESOProgrammeSummary
        lookup_field = "programme_id"

class HSTProgrammeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HSTProgrammeSummary
        lookup_field = "programme_id"


######################## Coordinates ########################

class CIRSCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CIRSCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'documentation', 'documentation_URL')

class FK4CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FK4Coordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'equinox', 'documentation', 'documentation_URL')

class FK4NoETermsCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FK4NoETermsCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'equinox', 'documentation', 'documentation_URL')

class FK5CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FK5Coordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'equinox', 'documentation', 'documentation_URL')

class GCRSCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCRSCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'documentation', 'documentation_URL')

class GalacticCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalacticCoordinates
        fields = ('l', 'l_unit', 'b', 'b_unit', 'documentation', 'documentation_URL')

class ICRSCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICRSCoordinates
        fields = ('ra', 'ra_unit', 'dec', 'dec_unit', 'documentation', 'documentation_URL')


######################## Conversions ########################

class CoordinatesConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatesConversion
        fields = ('input_first_value', 'input_second_value', 'input_frame', 'CIRS', 'FK4', 'FK4NoETerms',
                  'FK5', 'GCRS', 'Galactic', 'ICRS')

    CIRS = CIRSCoordinatesSerializer(required=False)
    FK4 = FK4CoordinatesSerializer(required=False)
    FK4NoETerms = FK4NoETermsCoordinatesSerializer(required=False)
    FK5 = FK5CoordinatesSerializer(required=False)
    GCRS = GCRSCoordinatesSerializer(required=False)
    Galactic = GalacticCoordinatesSerializer(required=False)
    ICRS = ICRSCoordinatesSerializer(required=False)


######################## Telegrams ########################

class AstronomersTelegramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AstronomersTelegram
        lookup_field = "identifier"
        fields = ('url', 'identifier', 'title', 'credential_certification', 'subjects', 'content', 'authors',
                  'external_links', 'related_telegrams', 'detected_objects')

    related_telegrams = AstronomersTelegramShortSerializer(required=False, many=True)
    detected_objects = AstronomicalObjectShortSerializer(required=False, many=True)
