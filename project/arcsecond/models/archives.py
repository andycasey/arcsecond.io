from django.core.validators import RegexValidator
from django.utils.timezone import utc
from django.db import models

from .constants import *
from .telescopes import *
from .observingsites import *
from .coordinates import AstronomicalCoordinates

class DataArchive(models.Model):
    class Meta: app_label = 'arcsecond'

    name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    organisations = models.ManyToManyField(AstronomicalOrganisation, blank=True, related_name='archive')


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


class ESOArchiveDataRowManager(models.Manager):
    def get_queryset(self):
        return super(ESOArchiveDataRowManager, self).get_queryset().order_by('-date')


class ESOArchiveDataRow(models.Model):
    class Meta: app_label = 'arcsecond'
    objects = ESOArchiveDataRowManager()

    summary = models.ForeignKey(ESOProgrammeSummary, null=True, blank=True, related_name='data_rows')
    archive = models.ForeignKey(DataArchive, null=True, blank=True, related_name='data_rows')
    object_field = models.CharField(max_length=100, null=True, blank=True)
    coordinates = models.ForeignKey(AstronomicalCoordinates, null=True, blank=True, related_name='eso_archive_data_rows')

    more_url = models.URLField()
    seeing_url = models.URLField()

    instrument_name = models.CharField(max_length=100, null=True, blank=True)
    telescope = models.ForeignKey(Telescope, null=True, blank=True, related_name='data_rows')

    dataset_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    exposure_time = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)


class FITSHeaderRow(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)
    data_row = models.ForeignKey(ESOArchiveDataRow, null=True, blank=True, related_name='header_rows')



class HSTProgrammeSummary(models.Model):
    class Meta: app_label = 'arcsecond'

    programme_id = models.CharField(max_length=20, primary_key=True)
    cycle = models.CharField(max_length=100, null=True, blank=True)
    allocation = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=500)

    principal_investigator = models.CharField(max_length=100)
    pi_institution = models.CharField(max_length=200)

    PROGRAM_TYPE_UNDEFINED = "(Undefined)"
    PROGRAM_TYPE_AR = "Archival Research"
    PROGRAM_TYPE_CAL = "Calibration program"
    PROGRAM_TYPE_ENG = "Engineering program"
    PROGRAM_TYPE_GO = "General Observer program"
    PROGRAM_TYPE_GODD = "Director's Discretionary program"
    PROGRAM_TYPE_GOPAR = "Pure parallel program"
    PROGRAM_TYPE_GTO = "Guaranteed Time Observer program"
    PROGRAM_TYPE_NASA = "Observing program conducted at the direction of NASA"
    PROGRAM_TYPE_SNAP = "Snapshot program"

    PROGRAM_TYPE_CHOICES = (
        (PROGRAM_TYPE_UNDEFINED, "(Undefined)"),
        (PROGRAM_TYPE_AR, "Archival Research"),
        (PROGRAM_TYPE_CAL, "Calibration program"),
        (PROGRAM_TYPE_ENG, "Engineering program"),
        (PROGRAM_TYPE_GO, "General Observer program"),
        (PROGRAM_TYPE_GODD, "Director's Discretionary program"),
        (PROGRAM_TYPE_GOPAR, "Pure parallel program"),
        (PROGRAM_TYPE_GTO, "Guaranteed Time Observer program"),
        (PROGRAM_TYPE_NASA, "Observing program conducted at the direction of NASA"),
        (PROGRAM_TYPE_SNAP, "Snapshot program"),
    )

    programme_type = models.CharField(max_length=100, choices=PROGRAM_TYPE_CHOICES, default=PROGRAM_TYPE_UNDEFINED)
    programme_type_auxiliary = models.CharField(max_length=100)

    PROGRAM_STATUS_UNDEFINED = "(Undefined)"
    PROGRAM_STATUS_PENDING_PHASE2_SUBMISSION = "Pending Phase II Submission"
    PROGRAM_STATUS_IMPLEMENTATION = "Implementation"
    PROGRAM_STATUS_SCHEDULING = "Scheduling"
    PROGRAM_STATUS_COMPLETED = "Program has been Completed"

    PROGRAM_STATUS_CHOICES = (
        (PROGRAM_STATUS_UNDEFINED, "(Undefined)"),
        (PROGRAM_STATUS_PENDING_PHASE2_SUBMISSION, "Pending Phase II Submission"),
        (PROGRAM_STATUS_IMPLEMENTATION, "Implementation"),
        (PROGRAM_STATUS_SCHEDULING, "Scheduling"),
        (PROGRAM_STATUS_COMPLETED, "Program has been Completed"),
    )

    programme_status = models.CharField(max_length=100, choices=PROGRAM_STATUS_CHOICES, default=PROGRAM_STATUS_UNDEFINED)
    abstract = models.CharField(max_length=5000, null=True, blank=True)

    related_programmes = models.ForeignKey('self', blank=True, null=True)