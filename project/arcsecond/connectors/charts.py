__author__ = 'onekiloparsec'

import xml
import urllib2
import feedparser

from django.utils import dateparse
from project.arcsecond.models import FindingChart, AstronomicalObject

IPAC_ROOT_URL = "http://irsa.ipac.caltech.edu/cgi-bin/FinderChart/nph-finder?mode=prog&locstr="

def get_OPTIR_charts(input):

    try:
        response = urllib2.urlopen(IPAC_ROOT_URL+urllib2.quote(input))
    except urllib2.URLError:
        return None

    finderchart = xml.etree.ElementTree.parse(response).getroot()

    raw_orientation = finderchart.find('input').find('orientation').text.lower()
    orientation = FindingChart.ORIENTATION_NORTHUP_EASTLEFT if (raw_orientation == "left") else FindingChart.ORIENTATION_NORTHUP_EASTRIGHT

    size = finderchart.find('input').find('subsetsize').text.split()[0]
    float_size = float(size)

    chart_pks = []
    for image in finderchart.find('result').iter('image'):

        raw_survey_name = image.find('surveyname').text.strip().lower()
        survey_name = FindingChart.SURVEY_NAME_UNDEFINED
        if raw_survey_name == "sdss":
            survey_name = FindingChart.SURVEY_NAME_SDSS
        elif raw_survey_name == "dss":
            survey_name = FindingChart.SURVEY_NAME_DSS
        elif raw_survey_name == "2mass":
            survey_name = FindingChart.SURVEY_NAME_TWOMASS

        band_name = image.find('band').text.strip()
        observing_date = dateparse.parse_date(image.find('obsdate').text.strip())
        fits_url = image.find('fitsurl').text.strip()
        image_url = image.find('jpgurl').text.strip()

        chart, created = FindingChart.objects.get_or_create(input=input, survey_name=survey_name, band_name=band_name,
                                                            orientation=orientation, size_unit=FindingChart.SIZE_UNIT_ARCMINUTES,
                                                            width=float_size, height=float_size, observing_date=observing_date,
                                                            fits_url=fits_url, image_url=image_url)

        obj, created = AstronomicalObject.objects.get_with_aliases_or_create(name=input)
        chart.astronomical_object = obj
        chart.save()

        chart_pks.append(chart.pk)

    return chart_pks
