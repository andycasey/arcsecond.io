# -- coding: utf-8 --

import xml
import urllib2
from project.arcsecond.models import *
from django.core.exceptions import MultipleObjectsReturned


ATEL_ROOT_URL = "http://www.astronomerstelegram.org/?read="
ATEL_REGEX = "(http:\/\/www\.astronomerstelegram\.org\/\?read\=[\d+])"
OBJECTS_REGEX = "(\W[A-Z]+[\d]?[\s]{,1}[a-zA-Z]?[\d\+\-\.]+\W)|(\W[\d]+[a-zA-Z]?[\s]{,1}[\w\+\-\.]+\W)"

NASA_ADS_ROOT_1 = "http://adsabs.harvard.edu/abs/"
NASA_ADS_ROOT_2 = "http://cdsads.u-strasbg.fr/abs/"
NASA_ADS_FORMAT_SUFFIX = "?data_type=XML"

def get_ADS_publication(bibcode):

    try:
        response = urllib2.urlopen(NASA_ADS_ROOT_1+urllib2.quote(bibcode)+NASA_ADS_FORMAT_SUFFIX)
    except urllib2.URLError:
        try:
            response = urllib2.urlopen(NASA_ADS_ROOT_2+urllib2.quote(bibcode)+NASA_ADS_FORMAT_SUFFIX)
        except urllib2.URLError:
            return None

    try:
        publication, created = Publication.objects.get_or_create(bibcode=bibcode)
    except MultipleObjectsReturned:
        return None

    publication.year = int(bibcode[:4])

    records = xml.etree.ElementTree.parse(response).getroot()
    ns = None
    if records.tag[0] == "{":
        namespace = records.tag[1:].split('}')[0]
        ns = {'ns': namespace}

    try:
        record = records[0]
    except IndexError:
        return None

    refereed_string = record.attrib.get("refereed", None)
    if refereed_string is not None:
        publication.is_refereed = (refereed_string.lower() == "true")

    pubtype_string = record.attrib.get("type", None)
    if pubtype_string is not None:
        if pubtype_string.lower() == "article":
            publication.publication_type = Publication.PUBLICATION_ARTICLE

    title_element = record.find('ns:title', ns)
    if title_element is not None:
        publication.title = title_element.text

    abstract_element = record.find('ns:abstract', ns)
    if abstract_element is not None:
        publication.abstract = abstract_element.text

    eprintid_element = record.find('ns:eprintid', ns)
    if eprintid_element is not None:
        publication.eprint_id = eprintid_element.text

    journal_element = record.find('ns:journal', ns)
    if journal_element is not None:
        values = journal_element.text.split(',')
        if len(values) > 2:
            publication.journal_name = values[0].strip()
            publication.volume_number = int(values[1].replace('Volume', ''))

    doi_element = record.find('ns:DOI', ns)
    if doi_element is not None:
        doi_string = doi_element.text
        doi_link, created = Link.objects.get_or_create(title=doi_string)
        doi_link.url = "http://dx.doi.org/"+doi_string
        doi_link.save()
        publication.doi = doi_link

    link_elements = record.findall('ns:link', ns)
    for link_element in link_elements:

        if link_element.attrib.get("type", "").lower() == 'references':
            ref_element = link_element
            ref_url = ref_element.find('ns:url', ns)
            try:
                ref_response = urllib2.urlopen(ref_url.text+"&data_type=SHORT_XML")
            except urllib2.URLError:
                pass
            else:
                ref_records = ref_response.read().split('<record>')
                for ref_record in ref_records:
                    start_index = ref_record.find('<bibcode>')
                    stop_index = ref_record.find('</bibcode>')
                    if start_index >= 0 and stop_index >= 0 and stop_index > start_index:
                        ref_bibcode = ref_record[start_index+len('<bibcode>'):stop_index]
                        ref_bibcode = ref_bibcode.replace('&amp;', '&')
                        ref_publication, created = Publication.objects.get_or_create(bibcode=ref_bibcode)
                        publication.references.add(ref_publication)

        if link_element.attrib.get("type", "").lower() == 'citations':
            cit_element = link_element
            cit_url = cit_element.find('ns:url', ns)
            try:
                cit_response = urllib2.urlopen(cit_url.text)
            except urllib2.URLError:
                pass
            else:
                cit_records = cit_response.read().split('<record>')
                for cit_record in cit_records:
                    start_index = ref_record.find('<bibcode>')
                    stop_index = ref_record.find('</bibcode>')
                    if start_index >= 0 and stop_index >= 0 and stop_index > start_index:
                        cit_bibcode = cit_record[start_index+len('<bibcode>'):stop_index]
                        cit_bibcode = cit_bibcode.replace('&amp;', '&')
                        cit_publication, created = Publication.objects.get_or_create(bibcode=cit_bibcode)
                        publication.citations.add(cit_publication)


    publication.save()
    return publication

