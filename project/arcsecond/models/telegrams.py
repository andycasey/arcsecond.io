from django.db import models
from multiselectfield import MultiSelectField

from .common import Link, Person
from .sky import AstronomicalObject

class AstronomersTelegram(models.Model):
    class Meta: app_label = 'arcsecond'

    identifier = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    credential_certification = models.CharField(max_length=500, null=True, blank=True)
    content = models.CharField(max_length=20000, null=True, blank=True)

    related_telegrams = models.ManyToManyField('self')

    authors = models.ManyToManyField(Person, related_name='astronomer_telegrams')
    external_links = models.ManyToManyField(Link, related_name='astronomer_telegrams')
    detected_objects = models.ManyToManyField(AstronomicalObject, related_name='astronomer_telegrams')

    SUBJECT_UNDEFINED = "unknown"
    SUBJECT_RADIO = "Radio"
    SUBJECT_MILLIMETER = "Millimeter"
    SUBJECT_SUBMILLIMETER = "Sub-Millimeter"
    SUBJECT_FARINFRARED = "Far-Infra-Red"
    SUBJECT_INFRARED = "Infra-Red"
    SUBJECT_OPTICAL = "Optical"
    SUBJECT_ULTRAVIOLET = "Ultra-Violet"
    SUBJECT_XRAY = "X-ray"
    SUBJECT_GAMMARAY = "Gamma Ray"
    SUBJECT_GEV = ">GeV"
    SUBJECT_TEV = "TeV"
    SUBJECT_VHE = "VHE"
    SUBJECT_UHE = "UHE"
    SUBJECT_NEUTRINOS = "Neutrinos"
    SUBJECT_COMMENT = "A Comment"
    SUBJECT_AGN = "AGN"
    SUBJECT_ASTEROID = "Asteroid"
    SUBJECT_ASTEROIDBINARY = "Asteroid (Binary)"
    SUBJECT_BINARY = "Binary"
    SUBJECT_BLACKHOLE = "Black Hole"
    SUBJECT_BLAZAR = "Blazar"
    SUBJECT_CATACLYSMICVAR = "Cataclysmic Variable"
    SUBJECT_COMET = "Comet"
    SUBJECT_COSMICRAYS = "Cosmic Rays"
    SUBJECT_GAMMARAYBURST = "Gamma-Ray Burst"
    SUBJECT_GLOBULARCLUSTER = "Globular Cluster"
    SUBJECT_GRAVITATIONALWAVES = "Gravitational Waves"
    SUBJECT_METEOR = "Meteor"
    SUBJECT_MICROLENSINGEVENT = "Microlensing Event"
    SUBJECT_NEAREARTHOBJECT = "Near-Earth Object"
    SUBJECT_NEUTRONSTAR = "Neutron Star"
    SUBJECT_NOVA = "Nova"
    SUBJECT_PLANET = "Planet"
    SUBJECT_PLANETMINOR = "Planet (minor)"
    SUBJECT_HAZARDOUSASTEROID = "Potentially Hazardous Asteroid"
    SUBJECT_PREMAINSEQSTAR = "Pre-Main-Sequence Star"
    SUBJECT_PULSAR = "Pulsar"
    SUBJECT_QUASAR = "Quasar"
    SUBJECT_REQFOROBS = "Request for Observations"
    SUBJECT_SOFTGAMMAREPEATER = "Soft Gamma-ray Repeater"
    SUBJECT_SOLARSYSTEMOBJECT = "Solar System Object"
    SUBJECT_STAR = "Star"
    SUBJECT_SUPERNOVAREMNANT = "Supernova Remnant"
    SUBJECT_SUPERNOVAE = "Supernovae"
    SUBJECT_SUN = "The Sun"
    SUBJECT_TRANSIENT = "Transient"
    SUBJECT_VARIABLES = "Variables"
    SUBJECT_YOUNGSTELLAROBJECT = "Young Stellar Object"

    SUBJECTS_KEYS = (SUBJECT_UNDEFINED, SUBJECT_RADIO, SUBJECT_MILLIMETER, SUBJECT_SUBMILLIMETER, SUBJECT_FARINFRARED, SUBJECT_INFRARED,
        SUBJECT_OPTICAL, SUBJECT_ULTRAVIOLET, SUBJECT_XRAY, SUBJECT_GAMMARAY, SUBJECT_GEV, SUBJECT_TEV, SUBJECT_VHE, SUBJECT_UHE, SUBJECT_NEUTRINOS,
        SUBJECT_COMMENT, SUBJECT_AGN, SUBJECT_ASTEROID, SUBJECT_ASTEROIDBINARY, SUBJECT_BINARY, SUBJECT_BLACKHOLE, SUBJECT_BLAZAR,
        SUBJECT_CATACLYSMICVAR, SUBJECT_COMET, SUBJECT_COSMICRAYS, SUBJECT_GAMMARAYBURST, SUBJECT_GLOBULARCLUSTER, SUBJECT_GRAVITATIONALWAVES,
        SUBJECT_METEOR, SUBJECT_MICROLENSINGEVENT, SUBJECT_NEAREARTHOBJECT, SUBJECT_NEUTRONSTAR, SUBJECT_NOVA, SUBJECT_PLANET, SUBJECT_PLANETMINOR,
        SUBJECT_HAZARDOUSASTEROID, SUBJECT_PREMAINSEQSTAR, SUBJECT_PULSAR, SUBJECT_QUASAR, SUBJECT_REQFOROBS, SUBJECT_SOFTGAMMAREPEATER,
        SUBJECT_SOLARSYSTEMOBJECT, SUBJECT_STAR, SUBJECT_SUPERNOVAREMNANT, SUBJECT_SUPERNOVAE, SUBJECT_SUN, SUBJECT_TRANSIENT,
        SUBJECT_VARIABLES, SUBJECT_YOUNGSTELLAROBJECT)

    SUBJECTS_VALUES = SUBJECTS_KEYS
    SUBJECTS_CHOICES = tuple(zip(SUBJECTS_KEYS, SUBJECTS_VALUES))
    subjects = MultiSelectField(choices=SUBJECTS_CHOICES, null=True)


class GCNCircular(models.Model):
    class Meta: app_label = 'arcsecond'

    identifier = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    content = models.CharField(max_length=20000, null=True, blank=True)
    submitter = models.ForeignKey(Person, null=True, blank=True, related_name='submitted_GCN_circulars')

    related_circulars = models.ManyToManyField('self')

    authors = models.ManyToManyField(Person, related_name='GCN_circulars')
    external_links = models.ManyToManyField(Link, related_name='GCN_circulars')
    detected_objects = models.ManyToManyField(AstronomicalObject, related_name='GCN_circulars')




