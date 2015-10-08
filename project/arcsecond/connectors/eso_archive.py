# -- coding: utf-8 --

import math
import decimal
import urllib2
import timestring

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from astropy.io import votable
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from project.arcsecond.models.archives import *
from project.arcsecond.models.coordinates import AstronomicalCoordinates
from project.arcsecond.models.constants import ESO_INSTRUMENTS

# ---------------- LOCAL CONSTANTS -----------------------------------

ESO_ARCHIVE_ROOT = "http://archive.eso.org/"
ESO_ARCHIVE_DB_ROOT = ESO_ARCHIVE_ROOT + "wdb/wdb/eso/eso_archive_main/query?"
ESO_ARCHIVE_WDBO = "wdbo="+urllib2.quote("votable/display")+"&"

ESO_ARCHIVE_MAX_ROWS = "10" if settings.DEBUG else "1000"
ESO_ARCHIVE_DEFAULT_PARAMS = "max_rows_returned="+ESO_ARCHIVE_MAX_ROWS+"&format=SexaHour&resolver=simbad&aladin_colour=aladin_instrument&tab_night=on&"

ESO_ARCHIVE_DEFAULT_ADDITIONAL_PARAMS = "tab_tel_airm_start=on&tab_stat_instrument=on&tab_ambient=on&tab_stat_exptime=on&tab_HDR=on&tab_mjd_obs=on&tab_stat_plot=on&tab_distance=on&tab_pos_angle=on&"
ESO_ARCHIVE_DEFAULT_TABS_PARAMS = "tab_target_coord=on&tab_object=on&tab_night=on&tab_prog_id=on&tab_gto=on&tab_obs_mode=on&tab_title=on&tab_dp_cat=on&tab_dp_tech=on&tab_dp_cat=on&tab_dp_type=on&tab_dp_tech=on&tab_dp_id=on&tab_rel_date=on&tab_exptime=on&tab_filter_path=on&tab_instrument=on&"

ESO_ARCHIVE_DEFAULT_SCIENCE_PARAM = "dp_cat=SCIENCE&"
ESO_ARCHIVE_DEFAULT_OBJECT_PARAM = "dp_type=OBJECT&"


# ------------------- DATA ROWS ---------------------------------------

def get_ESO_latest_data(science_only=True):

    url = ESO_ARCHIVE_DB_ROOT+ESO_ARCHIVE_WDBO+ESO_ARCHIVE_DEFAULT_PARAMS
    if science_only is True:
        url += ESO_ARCHIVE_DEFAULT_SCIENCE_PARAM

    archive, created = DataArchive.objects.get_or_create(name="ESO")

    offset = 0
    pks = []
    while len(pks) < 10:
        new_pks = read_ESO_VOTable_first_table(archive, offset)
        pks.extend(new_pks)
        print " •• Extending ESO archive rows by", len(new_pks), "pks, total:", len(pks)
        offset += 1

    return pks


def read_ESO_VOTable_first_table(archive, hour_offset=0):
    table = get_ESO_VOTable_first_table(hour_offset)

    if table is None:
        return []

    pks = []

    indices = {}
    for index, field in enumerate(table.fields):
        indices[field.name] = index

    summary_requests = []
    for row in xrange(len(table.array)):

        dataset_id = table.array[row][indices['dp_id']]
        data_row, created = ESOArchiveDataRow.objects.get_or_create(dataset_id=dataset_id)
        data_row.archive = archive

        instrument_name = table.array[row][indices['ins_id']]
        data_row.instrument_name = instrument_name

        ins_name = dataset_id.split('.')[0]
        date_string = dataset_id[len(ins_name)+1:]
        date_no_microseconds = timestring.Date(date_string, tz="UTC").date
        microseconds = int(date_string.split('.')[-1])*1000
        data_row.date = date_no_microseconds + timedelta(microseconds=microseconds)

        telescope_string = ESO_INSTRUMENTS[ins_name]["telescope"]
        try:
            telescope = Telescope.objects.get(name__contains=telescope_string)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            print ">>>>>> oh really???" + telescope_string
        else:
            data_row.telescope = telescope

        prog_id = table.array[row][indices['prog_id']]
        summary, created = ESOProgrammeSummary.objects.get_or_create(programme_id=prog_id)
        data_row.summary = summary
        if summary.period is None and prog_id not in summary_requests:
            summary_requests.append(prog_id)
            get_ESO_programme_id_summary(prog_id)

        # http://stackoverflow.com/questions/2569015/django-floatfield-or-decimalfield-for-currency
        if 'exptime' in indices.keys():
            exp_time = float(table.array[row][indices['exptime']])
            if not math.isnan(exp_time):
                data_row.exposure_time = decimal.Decimal(exp_time)

        if 'ra' in indices.keys() and 'dec' in indices.keys():
            ra = float(table.array[row][indices['ra']])
            dec = float(table.array[row][indices['dec']])
            if not math.isnan(ra) and not math.isnan(dec):
                coords, created = AstronomicalCoordinates.objects.get_or_create(right_ascension=ra, declination=dec)
                data_row.coordinates = coords

        if 'object' in indices.keys():
            data_row.object_field = table.array[row][indices['object']]

        data_row.save()
        pks.append(data_row.pk)

    return pks


def get_ESO_VOTable_first_table(hour_offset):
    url = ESO_ARCHIVE_DB_ROOT+ESO_ARCHIVE_WDBO+ESO_ARCHIVE_DEFAULT_PARAMS
    # Science only for now
    url += ESO_ARCHIVE_DEFAULT_SCIENCE_PARAM

    # Adding night param
    url += get_past_UTC_date_night(hour_offset)

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return None
    else:
        try:
            response_votable = votable.parse(response.fp)
            first_table = response_votable.get_first_table()
        except:
            return None
        else:
            return first_table


def get_past_UTC_date_night(hour_offset=0):
    utc_date_end   = datetime.now(tz=timezone.utc) - timedelta(hours=hour_offset)
    utc_date_start = datetime.now(tz=timezone.utc) - timedelta(hours=hour_offset+1)

    # +1 in hours is requested as ESO archive start at 1 and finish at 24.

    time_string_end_day  = "etime="  +urllib2.quote("{0} {1:02d} {2:02d}".format(utc_date_end.year, utc_date_end.month, utc_date_end.day))
    time_string_end_hour = "endtime="+urllib2.quote("{0:02d}".format(utc_date_end.hour+1))

    time_string_start_day  = "stime="    +urllib2.quote("{0} {1:02d} {2:02d}".format(utc_date_start.year, utc_date_start.month, utc_date_start.day))
    time_string_start_hour = "starttime="+urllib2.quote("{0:02d}".format(utc_date_start.hour+1))

    time_string = time_string_start_day +"&"+ time_string_start_hour +"&"+ time_string_end_day +"&"+ time_string_end_hour
    print " •• Getting ESO Data for time range: "+time_string
    return time_string



# ------------------- PROGRAMME SUMMARY ---------------------------------------

ESO_ARCHIVE_PROGRAMME_ID_URL_FORMAT = "wdb/wdb/eso/sched_rep_arc/query?wdbo=html&progid="

LINE_PERIOD_PREFIX = "Period................. "
LINE_OBSERVING_MODE_PREFIX = "Observing Mode......... "
LINE_PROGRAMME_TYPE_PREFIX = "Programme Type......... "
LINE_ALLOCATED_TIME_PREFIX = "Allocated time......... "
LINE_TELESCOPE_PREFIX = "Telescope.............. "
LINE_INSTRUMENT_PREFIX = "Instrument............. "
LINE_INVESTIGATORS_PREFIX = "PI/CoI................. "
LINE_PROP_TITLE_PREFIX = "Proposal Title......... "
LINE_REMARKS_PREFIX = "Remarks................ "
LINE_ABSTRACT_PREFIX = "Abstract............... "
LINE_OBSERVER_PREFIX = "Observer............... "
LINE_RAW_FILES_PREFIX = "Raw Files.............. "
LINE_PUBLICATIONS_PREFIX = "Publications........... "

ABSTRACT_LINE_CONTENT_PREFIX = "Abstract of proposal "


def get_ESO_programme_id_summary(programme_id):

    try:
        response = urllib2.urlopen(ESO_ARCHIVE_ROOT+ESO_ARCHIVE_PROGRAMME_ID_URL_FORMAT+urllib2.quote(programme_id))
    except urllib2.URLError:
        return None
    else:
        prog, created = ESOProgrammeSummary.objects.get_or_create(programme_id=programme_id)
        prog.programme_id = programme_id

        for line in response.readlines():
            if line.startswith(LINE_PERIOD_PREFIX):
                prog.period = line.replace(LINE_PERIOD_PREFIX, "").strip()

            elif line.startswith(LINE_OBSERVING_MODE_PREFIX):
                value = line.replace(LINE_OBSERVING_MODE_PREFIX, "").strip().lower()
                if 'service' in value:
                    prog.observing_mode = ESOProgrammeSummary.OBSERVING_MODE_SERVICE
                elif 'visitor' in value:
                    prog.observing_mode = ESOProgrammeSummary.OBSERVING_MODE_VISITOR

            elif line.startswith(LINE_PROGRAMME_TYPE_PREFIX):
                value = line.replace(LINE_PROGRAMME_TYPE_PREFIX, "").strip().lower()
                if 'normal' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_NORMAL
                elif 'guaranteed' in value or 'gto' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_GTO
                elif 'guaranteed' in value or 'gto' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_DDT
                elif 'opportunity' in value or 'too' in value or 'target' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_TOO
                elif 'large' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_LARGE
                elif 'short' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_SHORT
                elif 'calib' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_CALIB
                elif 'monitor' in value:
                    prog.programme_type = ESOProgrammeSummary.PROGRAM_TYPE_MONITOR

            elif line.startswith(LINE_ALLOCATED_TIME_PREFIX):
                prog.allocated_time = line.replace(LINE_ALLOCATED_TIME_PREFIX, "").strip()

            elif line.startswith(LINE_TELESCOPE_PREFIX):
                prog.telescope_name = line.replace(LINE_TELESCOPE_PREFIX, "").strip()

            elif line.startswith(LINE_INSTRUMENT_PREFIX):
                prog.instrument_name = line.replace(LINE_INSTRUMENT_PREFIX, "").strip()

            elif line.startswith(LINE_INVESTIGATORS_PREFIX):
                prog.investigators_list = line.replace(LINE_INVESTIGATORS_PREFIX, "").strip().decode('utf8')

            elif line.startswith(LINE_PROP_TITLE_PREFIX):
                prog.programme_title = line.replace(LINE_PROP_TITLE_PREFIX, "").strip().decode('utf8')

            elif line.startswith(LINE_REMARKS_PREFIX):
                prog.remarks = line.replace(LINE_REMARKS_PREFIX, "").decode('utf8').replace("<i>", "").replace("</i>", "").replace("&nbsp;", " ").strip()

            elif line.startswith(LINE_ABSTRACT_PREFIX):
                value = line.replace(LINE_ABSTRACT_PREFIX, "").strip()
                value_soup = BeautifulSoup(value, "html.parser")
                if value_soup.a is not None:
                    prog.abstract_url = ESO_ARCHIVE_ROOT+value_soup.a.get('href')
                    try:
                        abstract_response = urllib2.urlopen(prog.abstract_url+"&wdbo=ascii")
                    except urllib2.URLError:
                        pass
                    else:
                        for abstract_line in abstract_response.readlines():
                            if abstract_line.startswith(ABSTRACT_LINE_CONTENT_PREFIX):
                                prog.abstract = abstract_line.replace(ABSTRACT_LINE_CONTENT_PREFIX, "").strip().decode('utf8')
                                break

            elif line.startswith(LINE_OBSERVER_PREFIX):
                prog.remarks = line.replace(LINE_OBSERVER_PREFIX, "").strip().decode('utf8')

            elif line.startswith(LINE_RAW_FILES_PREFIX):
                value = line.replace(LINE_RAW_FILES_PREFIX, "").strip()
                value_soup = BeautifulSoup(value, "html.parser")
                if value_soup.a is not None:
                    prog.raw_files_url = ESO_ARCHIVE_ROOT+value_soup.a.get('href')

            elif line.startswith(LINE_PUBLICATIONS_PREFIX):
                value = line.replace(LINE_PUBLICATIONS_PREFIX, "").strip()
                value_soup = BeautifulSoup(value, "html.parser")
                if value_soup.a is not None:
                    prog.publications_url = value_soup.a.get('href')

        prog.save()
        return prog
