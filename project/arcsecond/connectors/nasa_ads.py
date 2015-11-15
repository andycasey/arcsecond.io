# -- coding: utf-8 --

import xml
import urllib2
import ads

from django.core.exceptions import MultipleObjectsReturned
from django.conf import settings

from project.arcsecond.models import *
from ._utils_ import *

ads.config.token = settings.ADS_CONFIG_TOKEN

ATEL_ROOT_URL = "http://www.astronomerstelegram.org/?read="
ATEL_REGEX = "(http:\/\/www\.astronomerstelegram\.org\/\?read\=[\d+])"

NASA_ADS_ROOT_1 = "http://adsabs.harvard.edu/abs/"
NASA_ADS_ROOT_2 = "http://cdsads.u-strasbg.fr/abs/"
NASA_ADS_FORMAT_SUFFIX = "?data_type=XML"

PUBLICATION_PROPERTY_OPENACCESS = 'OPENACCESS'
PUBLICATION_PROPERTY_REFEREED = 'REFEREED'
PUBLICATION_PROPERTY_NOT_REFEREED = 'NOT REFEREED'
PUBLICATION_PROPERTY_EPRINT_OPENACCESS = 'EPRINT_OPENACCESS'
PUBLICATION_PROPERTY_PUB_OPENACCESS = 'PUB_OPENACCESS'
PUBLICATION_PROPERTY_ADS_OPENACCESS = 'ADS_OPENACCESS'
PUBLICATION_PROPERTY_ARTICLE = 'ARTICLE'
PUBLICATION_PROPERTY_NONARTICLE = 'NONARTICLE'

def get_ADS_publication_from_bibcode(bibcode):
    if not re.match(bibcode_regex, bibcode):
        return None

    papers = list(ads.SearchQuery(bibcode=bibcode, sort="pubdate"))
    if len(papers) > 1:
        print "We get multiple papers for ADS bibcode", bibcode, " ???"
        return None

    publication = import_ADS_paper(papers[0])
    return publication

def get_ADS_publications_list_from_querystring(querystring):
    if re.match(bibcode_regex, querystring):
        publication = get_ADS_publication_from_bibcode(querystring)
        return [publication,] if publication is not None else None

    papers = list(ads.SearchQuery(q=querystring, sort="pubdate"))
    publications = []
    for paper in papers:
        publication = import_ADS_paper(paper)
        if publication is not None:
            publications.append(publication)

    return publications


def import_ADS_paper(paper):
    try:
        publication, created = Publication.objects.get_or_create(bibcode=paper.bibcode)
    except MultipleObjectsReturned:
        return None

    publication.abstract = paper.abstract
    publication.title = paper.title
    publication.keywords = paper.keyword
    publication.is_refereed = PUBLICATION_PROPERTY_REFEREED in paper.property

    for citation_bibcode in paper.citation: # yes, no plural...
        citation, created = Publication.objects.get_or_create(bibcode=citation_bibcode)
        publication.citations.add(citation)

    for reference_bibcode in paper.citation: # yes, no plural...
        reference, created = Publication.objects.get_or_create(bibcode=reference_bibcode)
        publication.references.add(reference)

    for organisation_name, author_name in zip(paper.aff, paper.author):
        name_elements = get_author_name(author_name)
        author, created = Person.objects.get_flexibly_or_create(**name_elements)
        publication.authors.add(author)

        organisation, created = Organisation.objects.get_or_create(name=organisation_name)
        affiliation, created = Affiliation.objects.get_or_create(person=author, organisation=organisation)

    if paper.pub.upper() == paper.pub:
        publisher, created = Publisher.objects.get_flexibly_or_create(acronym=paper.pub)
    else:
        publisher, created = Publisher.objects.get_flexibly_or_create(name=paper.pub)

    publication.journal = publisher
    publication.volume = paper.volume
    publication.year = paper.year

    publication.save()
    return publication

def get_ADS_publication_old(bibcode):

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

