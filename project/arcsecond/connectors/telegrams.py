# -- coding: utf-8 --

import re
import urllib2
import feedparser
import timestring

from email.utils import parseaddr
from bs4 import BeautifulSoup
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from project.arcsecond.models import AstronomersTelegram, GCNCircular, AstronomicalObject, Person

ATEL_ROOT_URL = "http://www.astronomerstelegram.org/?read="
ATEL_RSS_URL = "http://www.astronomerstelegram.org/?rss"
ATEL_REGEX = "(http:\/\/www\.astronomerstelegram\.org\/\?read\=[\d+])"

GCN_CIRCULAR_ROOT_URL_FORMAT = "http://gcn.gsfc.nasa.gov/gcn/gcn3/{0}.gcn3"

ATEL_OBJECTS_REGEX = "(\W[A-Z]+[\d]?[\s]{,1}[a-zA-Z]?[\d\+\-\.]+\W)|(\W[\d]+[a-zA-Z]?[\s]{,1}[\w\+\-\.]+\W)"
GCN_GRB_REGEX = "(GRB\s[0-9A-Z]+)"
GCN_GCN_CIRCULAR_REGEX = "(GCN\s?[0-9]+)"

def find_user_by_name(query_name):
   qs = Person.objects.all()
   for term in query_name.split():
     qs = qs.filter( Q(first_name__icontains = term) | Q(last_name__icontains = term))
   return qs

def find_objects_by_regex(regex_string, content_string):
    obj_tuples = re.findall(regex_string, content_string)
    delected_objects = []
    for obj_tuple in obj_tuples:
        obj_candidate_0 = obj_tuple[0].strip()
        obj_candidate_1 = obj_tuple[1].strip()

        if len(obj_candidate_0) > 0:
            if obj_candidate_0[0] == "(" and obj_candidate_0[-1] == ")":
                obj_candidate_0 = obj_candidate_0[1:-1]
            delected_objects.append(obj_candidate_0)

        if len(obj_candidate_1) > 0:
            if obj_candidate_1[0] == "(" and obj_candidate_1[-1] == ")":
                obj_candidate_1 = obj_candidate_1[1:-1]
            delected_objects.append(obj_candidate_1)

    final_objects = []
    for detect_obj in delected_objects:
        obj, created = AstronomicalObject.objects.get_with_aliases_or_create(name=detect_obj)
        final_objects.append(obj)

    return final_objects


def get_ATel(identifier):

    try:
        response = urllib2.urlopen(ATEL_ROOT_URL+urllib2.quote(identifier))
    except urllib2.URLError:
        return None
    else:
        atel, created = AstronomersTelegram.objects.get_or_create(identifier=identifier)

        soup = BeautifulSoup(response.read(), 'html.parser')

        telegram_tag = soup.find("div", id="telegram")
        title_tag = telegram_tag.find("h1", class_="title")
        if title_tag is not None:
            title = title_tag.string.strip()
            atel.title = title

            detected_objects = find_objects_by_regex(ATEL_OBJECTS_REGEX, title)
            for detected_obj in detected_objects:
                atel.detected_objects.add(detected_obj)

        subjects_tag = telegram_tag.find("div", id="subjects")
        if subjects_tag is not None:
            atel.subjects = subjects_tag.find("p").string.replace('Subjects:', '').strip()

        credentialsIndex = -1
        subjectsIndex = -1
        for index, text in enumerate(telegram_tag.stripped_strings):
            if 'Credential Certification' in text:
                credentialsIndex = index
            if 'Subjects:' in text:
                subjectsIndex = index

        contentText = ""
        startIndex = max(credentialsIndex, subjectsIndex)
        for index, text in enumerate(telegram_tag.stripped_strings):
            if index > startIndex and 'tweet' not in text.lower() and 'facebook' not in text.lower():
                contentText += text.strip()
                if text.strip()[-6:] != "ATel #" and not re.search("^([0-9]+)$", text.strip()) and not re.search("^http://[.*]", text.strip()):
                    contentText += "\n"

        if len(contentText) > 0:
            atel.content = contentText

        related_tag = soup.find("div", id="related") # Do NOT use telegram_tag
        if related_tag is not None:
            table = related_tag.table
            if table is not None:
                for tr in table.findAll("tr"):
                    tds = [td for td in tr.findAll('td')]
                    for td in tds:
                        a = td.find("a")
                        if a is not None:
                            if re.search(ATEL_REGEX, a['href']):
                                related_identifier = a['href'].replace(ATEL_ROOT_URL, '')
                                related_title = a.string.strip()

                                related_atel, created = AstronomersTelegram.objects.get_or_create(identifier=related_identifier)
                                related_atel.title = related_title
                                related_atel.save()

                                atel.related_telegrams.add(related_atel)

        atel.save()
        return atel


def read_last_ATels(page_size):
    try:
        response = urllib2.urlopen(ATEL_RSS_URL)
    except urllib2.URLError:
        return None
    else:
        rss = feedparser.parse(response.read())
        first_entry = rss['entries'][0]
        last_identifier = first_entry['identifier'].lower().replace('atel', '')

        for i in range(page_size):
            print 'Getting ATel'+last_identifier+'...'
            try:
                atel = AstronomersTelegram.objects.get(identifier=last_identifier)
            except ObjectDoesNotExist:
                get_ATel(last_identifier)
            last_identifier = str(int(last_identifier)-1)




def get_GCN_circular(identifier):
    try:
        response = urllib2.urlopen(GCN_CIRCULAR_ROOT_URL_FORMAT.format(urllib2.quote(identifier)))
    except urllib2.URLError:
        return None
    else:
        circular, created = GCNCircular.objects.get_or_create(identifier=identifier)
        content_lines = response.readlines()

        empty_line_count = 0
        gcn_content = ""

        for line in content_lines:
            if len(line.strip()) == 0:
                empty_line_count += 1

            if len(line) > 8 and line[:8] == "SUBJECT:":
                title = line[8:].strip()
                circular.title = title
                # Do NOT use find_by_regex, because this regex has only 1 matching group, it will return a list, not a list of tuples.
                detected_GRB_names = re.findall(GCN_GRB_REGEX, title)
                for detected_GRB_name in detected_GRB_names:
                    detected_obj, created = AstronomicalObject.objects.get_with_aliases_or_create(name=detected_GRB_name)
                    circular.detected_objects.add(detected_obj)

            elif len(line) > 5 and line[:5] == "DATE:":
                date_line = line[5:].strip()
                ymd = date_line.split(" ")[0]
                year = ymd.split("/")[0]
                prefix = "19" if float(year) > 80 else "20"
                circular.date = timestring.Date(prefix+date_line).date

            elif len(line) > 5 and line[:5] == "FROM:":
                submitted_line = line[5:].strip()
                raw_name, email = parseaddr(submitted_line)
                name = raw_name.split(' at ')[0]
                person_qs = find_user_by_name(name)
                if person_qs.count() == 1:
                    p = person_qs.first()
                    circular.submitter = p

            if empty_line_count >= 1:
                gcn_content += line.decode('utf-8', 'ignore')

        circular.content = gcn_content

        detected_GCN_identifiers = re.findall(GCN_GCN_CIRCULAR_REGEX, gcn_content)
        for detected_GCN_identifier in detected_GCN_identifiers:
            identifier = detected_GCN_identifier.replace('GCN', '').strip()
            detected_GCN, created = GCNCircular.objects.get_or_create(identifier=identifier)
            circular.related_circulars.add(detected_GCN)

        circular.save()
        return circular
