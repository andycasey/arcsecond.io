# coding=utf-8
from django.db import models
from multiselectfield import MultiSelectField
from .earth import *
from .observingsites import ObservingSite

class DomeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Dome(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = DomeManager()

    name = models.CharField(max_length=1000, null=True, blank=True)
    shape = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def natural_key(self):
        return self.name


class TelescopeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Telescope(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = TelescopeManager()

    def natural_key(self):
        return self.name

    name = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    acronym = models.CharField(max_length=100, null=True, blank=True)
    dome = models.OneToOneField(Dome, blank=True, null=True, related_name='telescope')
    observing_site = models.ForeignKey(ObservingSite, null=True, blank=True, related_name='telescopes')

    WAVELENGTH_DOMAIN_HARD_GAMMARAYS = "hga"
    WAVELENGTH_DOMAIN_WEAK_GAMMARAYS = "wga"
    WAVELENGTH_DOMAIN_HARD_XRAYS = "hxr"
    WAVELENGTH_DOMAIN_WEAK_XRAYS = "wxr"
    WAVELENGTH_DOMAIN_FAR_UV = "fuv"
    WAVELENGTH_DOMAIN_NEAR_UV = "nuv"
    WAVELENGTH_DOMAIN_OPTICAL = "opt"
    WAVELENGTH_DOMAIN_NEAR_INFRARED = "nir"
    WAVELENGTH_DOMAIN_MID_INFRARED = "mir"
    WAVELENGTH_DOMAIN_FAR_INFRARED = "fir"
    WAVELENGTH_DOMAIN_SUBMM = "smm"
    WAVELENGTH_DOMAIN_MM = "mmc"
    WAVELENGTH_DOMAIN_RADIO = "rad"

    WAVELENGTH_DOMAINS_KEYS = (
        WAVELENGTH_DOMAIN_HARD_GAMMARAYS,
        WAVELENGTH_DOMAIN_WEAK_GAMMARAYS,
        WAVELENGTH_DOMAIN_HARD_XRAYS,
        WAVELENGTH_DOMAIN_WEAK_XRAYS,
        WAVELENGTH_DOMAIN_FAR_UV,
        WAVELENGTH_DOMAIN_NEAR_UV,
        WAVELENGTH_DOMAIN_OPTICAL,
        WAVELENGTH_DOMAIN_NEAR_INFRARED,
        WAVELENGTH_DOMAIN_MID_INFRARED,
        WAVELENGTH_DOMAIN_FAR_INFRARED,
        WAVELENGTH_DOMAIN_SUBMM,
        WAVELENGTH_DOMAIN_MM,
        WAVELENGTH_DOMAIN_RADIO
    )

    WAVELENGTH_DOMAINS_VALUES = (
        "Hard gamma-rays",
        "Weak gamma-rays",
        "Hard x-rays",
        "Weak x-rays",
        "Far ultraviolet",
        "Near ultraviolet",
        "Optical",
        "Near infrared",
        "Mid-infrared",
        "Far infrared",
        "Sub-milimetric",
        "Milimetric",
        "Radio"
    )

    WAVELENGTH_DOMAINS_CHOICES = tuple(zip(WAVELENGTH_DOMAINS_KEYS, WAVELENGTH_DOMAINS_VALUES))
    wavelength_domains = MultiSelectField(choices=WAVELENGTH_DOMAINS_CHOICES)

    MOUNTING_UNDEFINED = "unk"
    MOUNTING_EQUATORIAL = "equ"
    MOUNTING_CASSEGRAIN = "cas"
    MOUNTING_ALTAZ = "aaz"
    MOUNTING_OFF_AXIS = "off"

    MOUNTING_KEYS = (
        MOUNTING_UNDEFINED,
        MOUNTING_EQUATORIAL,
        MOUNTING_CASSEGRAIN,
        MOUNTING_ALTAZ,
        MOUNTING_OFF_AXIS
    )

    MOUNTING_VALUES = (
        "Unknown",
        "Equatorial",
        "Cassegrain",
        "Alt-Az",
        "Off-Axis"
    )

    MOUNTING_CHOICES = tuple(zip(MOUNTING_KEYS, MOUNTING_VALUES))
    mounting = models.CharField(choices=MOUNTING_CHOICES, max_length=3, blank=True, default=MOUNTING_UNDEFINED)

    OPTICAL_DESIGN_UNDEFINED = "unk"
    OPTICAL_DESIGN_RITCHEY_CHRETIEN = "rc"
    OPTICAL_DESIGN_SCHMIDT = "sc"

    OPTICAL_DESIGNS_KEYS = (
        OPTICAL_DESIGN_UNDEFINED,
        OPTICAL_DESIGN_RITCHEY_CHRETIEN,
        OPTICAL_DESIGN_SCHMIDT
    )

    OPTICAL_DESIGNS_VALUES = (
        u"Unknown",
        u"Ritchey-Chrétien",
        u"Schmidt"
    )

    OPTICAL_DESIGNS_CHOICES = tuple(zip(OPTICAL_DESIGNS_KEYS, OPTICAL_DESIGNS_VALUES))
    optical_design = models.CharField(choices=OPTICAL_DESIGNS_CHOICES, max_length=3, default=OPTICAL_DESIGN_UNDEFINED, blank=True)

    has_active_optics = models.NullBooleanField()
    has_adaptative_optics = models.NullBooleanField()
    has_laser_guide_star = models.NullBooleanField()

    image_url = models.URLField(max_length=500, null=True, blank=True)
    image_url_copyright = models.CharField(max_length=100, null=True, blank=True)


class Mirror(models.Model):
    class Meta: app_label = 'arcsecond'

    telescope = models.ForeignKey(Telescope, blank=True, null=True, default=None, related_name='mirrors')
    mirror_index = models.IntegerField(null=True, blank=True, default=0)
    creation_date = models.DateField(null=True, blank=True)

    diameter = models.FloatField(null=True, blank=True)
    thickness = models.FloatField(null=True, blank=True)
    shape = models.CharField(max_length=100, null=True, blank=True)
    curvature = models.CharField(max_length=100, null=True, blank=True)
    coating = models.CharField(max_length=100, null=True, blank=True)
    central_obscuration = models.FloatField(null=True, blank=True)
    material = models.CharField(max_length=100, null=True, blank=True)


