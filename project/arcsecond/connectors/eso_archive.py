# -- coding: utf-8 --

import urllib2

from astropy.io import votable
from bs4 import BeautifulSoup
from datetime import datetime

from project.arcsecond.models import ESOProgrammeSummary, ESOArchiveDataRow

ESO_ARCHIVE_ROOT = "http://archive.eso.org/"
ESO_ARCHIVE_DB_ROOT = ESO_ARCHIVE_ROOT + "wdb/wdb/eso/eso_archive_main/query?wdbo=votable/display&"
ESO_ARCHIVE_DEFAULT_PARAMS = "resolver=simbad&format=SexaHour&"
ESO_ARCHIVE_DEFAULT_ADDITIONAL_PARAMS = "tab_tel_airm_start=on&tab_stat_instrument=on&tab_ambient=on&tab_stat_exptime=on&tab_HDR=on&tab_mjd_obs=on&tab_stat_plot=on&tab_distance=on&tab_pos_angle=on&"
ESO_ARCHIVE_DEFAULT_TABS_PARAMS = "tab_target_coord=on&tab_object=on&tab_night=on&tab_prog_id=on&tab_gto=on&tab_obs_mode=on&tab_title=on&tab_dp_cat=on&tab_dp_tech=on&tab_dp_cat=on&tab_dp_type=on&tab_dp_tech=on&tab_dp_id=on&tab_rel_date=on&tab_exptime=on&tab_filter_path=on&tab_instrument=on&"
ESO_ARCHIVE_DEFAULT_SCIENCE_PARAMS = "dp_cat=SCIENCE&dp_type=OBJECT&"


# ------------------- DATA ROWS ---------------------------------------

def get_ESO_latest_data(start_date=None, end_date=None, science_only=True):
    url = ESO_ARCHIVE_DB_ROOT+ESO_ARCHIVE_DEFAULT_PARAMS+ESO_ARCHIVE_DEFAULT_ADDITIONAL_PARAMS+ESO_ARCHIVE_DEFAULT_TABS_PARAMS
    if science_only is True:
        url += ESO_ARCHIVE_DEFAULT_SCIENCE_PARAMS

    url += "max_rows_returned=10&starttime=12&endtime=12&"

    utc_date = datetime.utcnow()
    url += urllib2.quote("night={0} {1} {2}&".format(utc_date.year, utc_date.month, utc_date.day))

    print url

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

        dataset_id_index = -1
        for index, field in enumerate(first_table.fields):
            if field.name == 'dp_id':
                dataset_id_index = index

        pks = []
        for row in xrange(len(first_table.array)):
            dataset_id = first_table.array[row][dataset_id_index]
            data_row, created = ESOArchiveDataRow.objects.get_or_create(dataset_id=dataset_id)
            pks.append(data_row.pk)

        return pks





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
                prog.abstract_url = ESO_ARCHIVE_ROOT+value_soup.a.get('href')

                try:
                    abstract_response = urllib2.urlopen(prog.abstract_url+"&wdbo=ascii")
                except urllib2.URLError:
                    return None
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
                prog.raw_files_url = ESO_ARCHIVE_ROOT+value_soup.a.get('href')

            elif line.startswith(LINE_PUBLICATIONS_PREFIX):
                value = line.replace(LINE_PUBLICATIONS_PREFIX, "").strip()
                value_soup = BeautifulSoup(value, "html.parser")
                prog.publications_url = value_soup.a.get('href')

        prog.save()
        return prog
