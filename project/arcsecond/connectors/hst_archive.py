# -- coding: utf-8 --

import urllib2
from bs4 import BeautifulSoup
from project.arcsecond.models import HSTProgrammeSummary

STSCI_ARCHIVE_ROOT = "http://www.stsci.edu/cgi-bin/get-proposal-info"
STSCI_ARCHIVE_PROGRAMME_ID_FORMAT = "id="
STSCI_ARCHIVE_OBSERVATORY_FORMAT = "observatory="

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


def get_STSCI_programme_id_summary(observatory, programme_id):

    url = STSCI_ARCHIVE_ROOT
    url += "?" + STSCI_ARCHIVE_OBSERVATORY_FORMAT + urllib2.quote(observatory)
    url += "&" + STSCI_ARCHIVE_PROGRAMME_ID_FORMAT + urllib2.quote(programme_id)

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return None
    else:
        prog, created = HSTProgrammeSummary.objects.get_or_create(programme_id=programme_id)
        prog.programme_id = programme_id

        soup = BeautifulSoup(response.read(), "html.parser")
        # programme_id = soup.h1.contents[-1].strip()

        # print(soup.prettify())
        current = soup.p.contents
        if 'principal' in current[0].string.lower() and 'investigator' in current[0].string.lower():
            prog.programme_principal_investigator = current[1].strip()

        prog.save()
        return prog

