from rest_framework import serializers
from rest_framework.reverse import reverse
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

class GCNCircularShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCNCircular
        lookup_field = "identifier"
        fields = ('url', 'identifier')

class PublicationShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        lookup_field = "bibcode"
        fields = ('url', 'bibcode')

class TelescopeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telescope
        lookup_field = "name"
        fields = ('url', 'name')


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
        fields = ("bibcode", "eprint_id", "title", "year", "publication_type", "publication_date", "journal_name",
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


class DistanceSerializer(serializers.ModelSerializer):
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

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('longitude', 'latitude', 'height')

######################## Observing Sites ########################


class ObservingSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservingSite
        lookup_field = "name"
        fields = ('name', 'long_name', 'IAUCode', 'continent', 'coordinates', 'address_line_1', 'address_line_2',
                  'zip_code', 'country', 'time_zone', 'time_zone_name', 'telescopes')

    coordinates = CoordinatesSerializer()
    telescopes = serializers.HyperlinkedRelatedField(many=True,
                                                     read_only=True,
                                                     view_name='telescope-detail',
                                                     lookup_field='name')

######################## Telescopes ########################

class DomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dome
        fields = ('name', 'shape', 'image')

class MirrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mirror
        fields = ('mirror_index', 'diameter')

class TelescopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telescope
        lookup_field = "name"
        fields = ('name', 'acronym', 'observing_site', 'mounting', 'optical_design', 'has_active_optics',
                  'has_adaptative_optics', 'has_laser_guide_star', 'wavelength_domains', 'dome', 'mirrors')

    observing_site = serializers.HyperlinkedRelatedField(read_only=True,
                                                         view_name='observingsite-detail',
                                                         lookup_field='name')

    dome = DomeSerializer(required=False)
    mirrors = MirrorSerializer(required=False, many=True)

    wavelength_domains = serializers.SerializerMethodField()
    mounting = serializers.SerializerMethodField()
    optical_design = serializers.SerializerMethodField()

    def get_wavelength_domains(self, obj):
        return [Telescope.WAVELENGTH_DOMAINS_VALUES[Telescope.WAVELENGTH_DOMAINS_KEYS.index(domain)] for domain in obj.wavelength_domains]

    def get_mounting(self, obj):
        return Telescope.MOUNTING_VALUES[Telescope.MOUNTING_KEYS.index(obj.mounting)]

    def get_optical_design(self, obj):
        return Telescope.OPTICAL_DESIGNS_VALUES[Telescope.OPTICAL_DESIGNS_KEYS.index(obj.optical_design)]



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

    planets = serializers.HyperlinkedRelatedField(many=True,
                                                  read_only=True,
                                                  view_name='exoplanet-named-detail',
                                                  lookup_field='name')

    astronomer_telegrams = AstronomersTelegramShortSerializer(required=False, many=True)

    finding_charts = serializers.HyperlinkedIdentityField(view_name='findingchart-list',
                                                          lookup_field='name',
                                                          lookup_url_kwarg='input',
                                                          read_only=True,
                                                          required=False)

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

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ('code', 'message')

class CoordinatesConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatesConversion
        fields = ('input_first_value', 'input_second_value', 'input_frame', 'error',
                  'CIRS', 'FK4', 'FK4NoETerms', 'FK5', 'GCRS', 'Galactic', 'ICRS')

    error = ErrorSerializer(required=False)

    CIRS = CIRSCoordinatesSerializer(required=False)
    FK4 = FK4CoordinatesSerializer(required=False)
    FK4NoETerms = FK4NoETermsCoordinatesSerializer(required=False)
    FK5 = FK5CoordinatesSerializer(required=False)
    GCRS = GCRSCoordinatesSerializer(required=False)
    Galactic = GalacticCoordinatesSerializer(required=False)
    ICRS = ICRSCoordinatesSerializer(required=False)


class TimesConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimesConversion
        fields = ('input_format', 'input_value', 'documentation_URL', 'error', 'byear', 'byear_str', 'cxcsec', 'datetime',
                  'decimalyear', 'gps', 'iso', 'isot', 'jd', 'jyear', 'jyear_str', 'mjd', 'plot_date', 'unix', 'yday')

    error = ErrorSerializer(required=False)

######################## Telegrams ########################

class AstronomersTelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomersTelegram
        lookup_field = "identifier"
        fields = ('identifier', 'title', 'credential_certification', 'subjects', 'content', 'authors',
                  'related_telegrams', 'detected_objects', 'external_links')

    related_telegrams = serializers.HyperlinkedRelatedField(many=True,
                                                            read_only=True,
                                                            view_name='astronomerstelegram-detail',
                                                            lookup_field='identifier')

    detected_objects = serializers.HyperlinkedRelatedField(many=True,
                                                           read_only=True,
                                                           view_name='astronomicalobject-detail',
                                                           lookup_field='name')


class GCNCircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCNCircular
        lookup_field = "identifier"
        fields = ('identifier', 'title', 'date', 'content', 'submitter', 'authors',
                  'related_circulars', 'external_links')

    submitter = PersonSerializer(required=False)
    related_circulars = serializers.HyperlinkedRelatedField(many=True,
                                                            read_only=True,
                                                            view_name='gcncircular-detail',
                                                            lookup_field='identifier')



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
