#!/Users/onekiloparsec/.virtualenvs/iobs-debug/bin/python
# -*- coding: utf-8 -*-

__author__ = 'onekiloparsec'

import os
import sys
sys.path.append(".")

import django
django.setup()


from project.arcsecond.models.accounts import *
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

for user in get_user_model().objects.all():
	try:
		profile = user.profile
	except ObjectDoesNotExist:
		print user, 'has no profile. Creating.'
		profile = UserProfile.objects.create(user=user)
	else:
		print user, 'is OK'
	
	
