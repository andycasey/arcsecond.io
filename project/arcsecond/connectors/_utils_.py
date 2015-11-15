
import re
from project.arcsecond.models.constants import *

def get_author_name(author_name):
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
    return {'first_name':first_name, 'initials':initials, 'last_name':last_name}
