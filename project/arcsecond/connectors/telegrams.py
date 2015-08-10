# -- coding: utf-8 --

import re
import urllib2
from bs4 import BeautifulSoup

from project.arcsecond.models import AstronomersTelegram

ATEL_ROOT_URL = "http://www.astronomerstelegram.org/?read="
ATEL_REGEX = "(http:\/\/www\.astronomerstelegram\.org\/\?read\=[\d+])"

def get_ATel(identifier):

    try:
        response = urllib2.urlopen(ATEL_ROOT_URL+urllib2.quote(identifier))
    except urllib2.URLError:
        return None
    else:
        atel, created = AstronomersTelegram.objects.get_or_create(identifier=identifier)

        soup = BeautifulSoup(response.read(), 'html.parser')
        related_table = soup.find("div", id="related")
        if related_table is not None:
            table = related_table.table
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


