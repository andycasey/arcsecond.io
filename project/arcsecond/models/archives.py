from django.core.validators import RegexValidator
from django.db import models
from constants import *

class ESOProgrammeSummary(models.Model):
    class Meta: app_label = 'arcsecond'

    programme_id = models.CharField(max_length=20, primary_key=True, validators=[RegexValidator(regex=eso_programme_id_regex, message='Invalid ESO Programme ID', code='nomatch')])
    period = models.CharField(max_length=100, null=True, blank=True)

    OBSERVING_MODE_UNDEFINED = "(Undefined)"
    OBSERVING_MODE_VISITOR = "Visitor"
    OBSERVING_MODE_SERVICE = "Service"

    OBSERVING_MODE_CHOICES = (
        (OBSERVING_MODE_UNDEFINED, '(Undefined)'),
        (OBSERVING_MODE_VISITOR, 'Visitor'),
        (OBSERVING_MODE_SERVICE, 'Service'),
    )

    observing_mode = models.CharField(max_length=100, choices=OBSERVING_MODE_CHOICES, default=OBSERVING_MODE_UNDEFINED)

    PROGRAM_TYPE_UNDEFINED = "(Undefined)"
    PROGRAM_TYPE_NORMAL = "Normal Programme"
    PROGRAM_TYPE_GTO = "Guaranteed Time Observations"
    PROGRAM_TYPE_DDT = "Director's Discretionary Time"
    PROGRAM_TYPE_TOO = "Target of Opportunity"
    PROGRAM_TYPE_LARGE = "Large Programme"
    PROGRAM_TYPE_SHORT = "Short Programme"
    PROGRAM_TYPE_CALIB = "Calibration Programme"
    PROGRAM_TYPE_MONITOR = "Monitoring Programme"

    PROGRAM_TYPE_CHOICES = (
        (PROGRAM_TYPE_UNDEFINED, "(Undefined)"),
        (PROGRAM_TYPE_NORMAL, "Normal Programme"),
        (PROGRAM_TYPE_GTO, "Guaranteed Time Observations"),
        (PROGRAM_TYPE_DDT, "Director's Discretionary Time"),
        (PROGRAM_TYPE_TOO, "Target of Opportunity"),
        (PROGRAM_TYPE_LARGE, "Large Programme"),
        (PROGRAM_TYPE_SHORT, "Short Programme"),
        (PROGRAM_TYPE_CALIB, "Calibration Programme"),
        (PROGRAM_TYPE_MONITOR, "Monitoring Programme"),
    )

    programme_type = models.CharField(max_length=100, choices=PROGRAM_TYPE_CHOICES, default=PROGRAM_TYPE_UNDEFINED)

    allocated_time = models.CharField(max_length=100, null=True, blank=True)
    telescope_name = models.CharField(max_length=100, null=True, blank=True)
    instrument_name = models.CharField(max_length=100, null=True, blank=True)

    investigators_list = models.CharField(max_length=500, null=True, blank=True)
    programme_title = models.CharField(max_length=500, null=True, blank=True)
    remarks = models.CharField(max_length=500, null=True, blank=True)

    abstract_url = models.URLField(max_length=500, null=True, blank=True)
    abstract = models.CharField(max_length=5000, null=True, blank=True)

    observer_name = models.CharField(max_length=500, null=True, blank=True)
    raw_files_url = models.URLField(max_length=500, null=True, blank=True)
    publications_url = models.URLField(max_length=500, null=True, blank=True)


