# -- coding: utf-8 --

import re
import xml
import urllib2
from django.core.exceptions import ObjectDoesNotExist
import feedparser
from bs4 import BeautifulSoup

from project.arcsecond.models import AstronomersTelegram, AstronomicalObject

ATEL_ROOT_URL = "http://www.astronomerstelegram.org/?read="
ATEL_RSS_URL = "http://www.astronomerstelegram.org/?rss"

ATEL_REGEX = "(http:\/\/www\.astronomerstelegram\.org\/\?read\=[\d+])"
OBJECTS_REGEX = "(\W[A-Z]+[\d]?[\s]{,1}[a-zA-Z]?[\d\+\-\.]+\W)|(\W[\d]+[a-zA-Z]?[\s]{,1}[\w\+\-\.]+\W)"

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

            obj_tuples = re.findall(OBJECTS_REGEX, title)
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

            for detect_obj in delected_objects:
                obj, created = AstronomicalObject.objects.get_or_create(name=detect_obj)
                atel.detected_objects.add(obj)
                obj.save()

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





