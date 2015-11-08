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
				latitude = math.degrees(math.atan2(C, S)) # not atan2(S, C), there is a mistake in doc
			else:
				if S == 0.0:
					latitude = math.degrees(math.atan(1.0))
				else:
					print '?????'
					print line
					sys.exit(1)
				
			if longitude > 180.0:
				longitude -= 360.0
			if longitude < -180:
				longitude += 360.0

			if latitude > 90.0:
				latitude -= 180.0
			if latitude < -90:
				latitude += 180.0
				
			print '('+code+')', name, longitude, latitude
						
			try:
				site = ObservingSite.objects.get(IAUCode=code)
			except Exception:
				# No site with such IAO code. Let's try with coordinates.
				coords, created = Coordinates.objects.get_or_create(longitude=longitude, latitude=latitude, height=height)					
								
				# We get coordinates. Testing against site or 'created' bool is identical.
				if 'site' not in coords._meta.get_all_field_names() and created is False:
					print "coordinates are used for something else???"
					print site, code, name, "\n\n\n"
					sys.exit(1)
					
				if created:
					# New coordinates. Create the associated site, and associated coords to it.
					site = ObservingSite.objects.create(IAUCode=code)
					site.coordinates = coords
					site.save()
				else:
					# Coordinates exists. Hence, look for site (which may have no IAU code yet).
					try:
						site = coords.site
					except Exception:
						# should be rare
						site = ObservingSite.objects.create(IAUCode=code)
						site.coordinates = coords
						site.save()
					else:
						site.IAUCode = code
						site.save()
					
			else:
				# We have a site.
				if site.coordinates is None:
					# We don't have yet coordinates??
					coords, created = Coordinates.objects.get_or_create(longitude=longitude, latitude=latitude, height=height)					
					if created is False:
						# Conflicting sites with different names. Do not update.
						print '--- Not created!', coords.site
					else:
						site.coordinates = coords				
						site.save()
				else:
					pass # Do NOT update coordinates, as MPC data are not as good as iObserve's

			if site.name is None:
				site.name = name
			elif site.name != name:
				site.alternate_name_1 = name
				
			if site.sources is None:
				site.sources = ['MPC']
			elif 'MPC' not in site.sources:
				site.sources += ['MPC']
			
			site.save()
				
				
				
				
						
			