#!/usr/bin/env python
# -* coding: utf-8 *-

import re
name_intials_regex = u"([A-Z]{1}[a-z]?\.(\s?\-?[A-Z]{1}[a-z]?\.)?)"

names = [u'Chenevez, J.', u'Brandt, S.', u'Kuulkers, E.', u'Alfonso-Garz\u0e23\u0e13n, J.', u'Beckmann, V.', u'Bird, T.', u'Courvoisier, Th.', u'Del Santo, M.', u'Domingo, A.', u'Ebisawa, K.', u'Jonker, P.', u'Kretschmar, P.', u'Markwardt, C.', u'Oosterbroek, T.', u'Paizis, A.', u'Pottschmidt, K.', u'S\u0e23\u0e01nchez-Fern\u0e23\u0e01ndez, C.', u'Wijnands, R.', u'Courvoisier, Thierry J. -L.']


for author_name in names:
    name_elements = author_name.split(',')
    last_name = name_elements[0]
    initials = []
    cleaned_name_elements = []
    for name_element in name_elements[1:]:
        initials_candidate_groups = re.findall(name_intials_regex, name_element)
        cleaned_name_element = name_element
        for group in initials_candidate_groups:
            initials_first_group = group[0] if type(group) is tuple else group
            initials.append(initials_first_group)
            cleaned_name_element = cleaned_name_element.replace(initials_first_group, '')
        if len(cleaned_name_element.strip()) > 0:
            cleaned_name_elements.append(cleaned_name_element.replace(',','').strip())
            
    first_name = cleaned_name_elements[0] if len(cleaned_name_elements) > 0 else None

    print u'Last: ', last_name
    print u'Initials: ', initials
    print u'First: ', first_name
    print '----------'