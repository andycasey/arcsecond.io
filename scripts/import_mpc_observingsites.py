#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'onekiloparsec'

import os
import sys
sys.path.append(".")

import django
django.setup()

import math
import traceback

from project.arcsecond.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

with open('scripts/mpc_observatories.csv', 'r') as x:
	lines = x.readlines()
	index = 2000
	
	for line in lines:
		if len(line.strip()) > 0 and line[0] != '#':
			elements = line.strip().split(',')
			code = elements[0]
			longitude = float(elements[1])
			cosphip = elements[2]
			sinphip = elements[3]
			gclat = elements[4]
			gdlat = elements[5]
			height = float(elements[6])
			
			name = elements[7].strip()
			if len(elements) > 8:
				name += ", "
				name += elements[8].strip()	
			name = name.replace('"', '')
							
			S = float(cosphip)
			C = float(sinphip)
			if C != 0.0:
				latitude = math.atan(S/C)
			else:
				if S == 0.0:
					latitude = math.atan(1.0)
				else:
					print '?????'
					print line
					sys.exit(1)
				
			print '('+code+')', name
						
			try:
				site = ObservingSite.objects.get(IAUCode=code)
			except Exception:
				coords, created = Coordinates.objects.get_or_create(longitude=longitude, latitude=latitude, height=height)					
				if coords.site is None:
					if created:
						site = ObservingSite.objects.create(IAUCode=code)
						site.coordinates = coords
					else:
						print "coordinates are used for something else???"
						print site, code, name, "\n\n\n"
						sys.exit(1)
				else:
					site = coords.site				
								
			if site.name is None:
				site.name = name
			elif site.name != name:
				site.alternate_name_1 = name
				
			if site.sources is None:
				site.sources = ['MPC']
			else:
				site.sources += ['MPC']
			
			try:
				site.save()
			except Exception:
				traceback.print_exc()
				print site, code, name, "\n\n\n"
				# sys.exit(1)
				
				
				
				
						
			