from rest_framework import serializers
from project.arcsecond.models import Telescope, Mirror, Dome

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
        fields = ('id', 'name', 'acronym', 'observing_site', 'mounting', 'optical_design', 'has_active_optics',
                  'has_adaptative_optics', 'has_laser_guide_star', 'wavelength_domains', 'dome', 'mirrors')

    observing_site = serializers.HyperlinkedRelatedField(read_only=True,
                                                         view_name='observingsite-named-detail',
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



