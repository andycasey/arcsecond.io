__author__ = 'onekiloparsec'

import xml
import urllib2
import feedparser
from bs4 import BeautifulSoup
from project.arcsecond.models import FindingChart

IPAC_ROOT_URL = "http://irsa.ipac.caltech.edu/cgi-bin/FinderChart/nph-finder?mode=prog&locstr="

def get_OPTIR_charts(input):

    try:
        response = urllib2.urlopen(IPAC_ROOT_URL+urllib2.quote(input))
    except urllib2.URLError:
        return None

    chart, created = FindingChart.objects.get_or_create(input=input)

    response_string = response.read()
    finderchart = xml.etree.ElementTree.parse(response_string).getroot()
    parser = feedparser.parse(response_string)

    ns = None
    if finderchart.tag[0] == "{":
        namespace = finderchart.tag[1:].split('}')[0]
        ns = {'ns': namespace}


    return None
