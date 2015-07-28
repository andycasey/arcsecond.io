# -- coding: utf-8 --

import urllib2
import xml
from bs4 import BeautifulSoup
from project.arcsecond.models import HSTProgrammeSummary

STSCI_ARCHIVE_PROPINFO_ROOT = "http://www.stsci.edu/cgi-bin/get-proposal-info"
STSCI_ARCHIVE_PROGRAMME_ID_FORMAT = "id="
STSCI_ARCHIVE_OBSERVATORY_FORMAT = "observatory="

STSCI_ARCHIVE_PHASE2_ROOT_FORMAT = "http://www.stsci.edu/%s/phase2-public/%s.apt"

def get_STSCI_programme_id_summary(observatory, programme_id):

    url = STSCI_ARCHIVE_PHASE2_ROOT_FORMAT%(observatory.lower(), programme_id)

    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        return None
    else:
        prog, created = HSTProgrammeSummary.objects.get_or_create(programme_id=programme_id)
        prog.programme_id = programme_id

        e = xml.etree.ElementTree.parse(response).getroot()
        info = e.find("ProposalInformation")

        category = info.get("Category")
        if category == "GO":
            prog.programme_type = HSTProgrammeSummary.PROGRAM_TYPE_GO

        prog.cycle = info.get("Cycle")
        prog.title = info.find("Title").text
        prog.abstract = info.find("Abstract").text

        pi = info.find("PrincipalInvestigator")
        prog.principal_investigator = pi.get("Honorific") +" "+ pi.get("FirstName") +" "+ pi.get("LastName")

        prog.save()
        return prog

