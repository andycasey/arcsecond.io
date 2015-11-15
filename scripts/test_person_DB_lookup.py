#!/Users/onekiloparsec/.virtualenvs/iobs-debug/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(".")

import django
django.setup()

from project.arcsecond.models import *
from django.core.exceptions import ObjectDoesNotExist

# Person.objects.create(last_name="Last1")
# Person.objects.create(last_name="Last2", first_name="First2")
# Person.objects.create(last_name="Last3", first_name="First3", initials=["A.", "B.", "C.-D."])

print 'Looking for person with last_name Last3 (valid)'
print Person.objects.get_flexibly_or_create(last_name="Last3")

print 'Looking for person with last_name Last3, initials=["A."], valid'
print Person.objects.get_flexibly_or_create(last_name="Last3", initials=["A."])

print 'Looking for person with last_name Last3, initials=["Z."], invalid'
print Person.objects.get_flexibly_or_create(last_name="Last3", initials=["Z."])

