# -- coding: utf-8 --

import urllib2
from bs4 import BeautifulSoup
from project.arcsecond.models import ESOProgrammeSummary

ESO_ARCHIVE_ROOT = "http://archive.eso.org/"
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
                prog.publications_url = ESO_ARCHIVE_ROOT+value_soup.a.get('href')

        prog.save()
        return prog
