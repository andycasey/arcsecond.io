#!/Users/onekiloparsec/.virtualenvs/iobs-debug/bin/python
# -*- coding: utf-8 -*-

__author__ = 'onekiloparsec'

import os
import sys
sys.path.append(".")

import django
django.setup()


from project.arcsecond.models.observingsites import *
from django.core.exceptions import ObjectDoesNotExist

for obssite in ObservingSite.objects.all():
	if obssite.sources is None:
		print obssite
		obssite.sources = ['iObserve']
		obssite.save()
		
	
