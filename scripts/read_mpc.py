#!/usr/bin/env python

import math

with open('../project/arcsecond/fixtures/mpc.json', 'w') as f:
	f.write('[\n')
	
	with open('mpc_observatories.csv', 'r') as x:
		lines = x.readlines()
		index = 2000
		
		for line in lines:
			if len(line.strip()) > 0 and line[0] != '#':
				elements = line.strip().split(',')
				code = elements[0]
				longitude = elements[1]
				cosphip = elements[2]
				sinphip = elements[3]
				gclat = elements[4]
				gdlat = elements[5]
				height = elements[6]
				
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
				
				f.write('{\n')
				f.write('\t\"pk\" : '+str(index)+', \n')
				f.write('\t\"model\" : \"arcsecond.Coordinates\", \n')
				f.write('\t\"fields\" : {\n')
				f.write('\t\t\"latitude\": '+str(latitude)+',\n')
				f.write('\t\t\"longitude\": '+longitude+',\n')
				f.write('\t\t\"height\": '+height+'\n')
				f.write('\t}\n')
				f.write('},\n')

				f.write('{\n')
				f.write('\t\"pk\" : '+str(index)+', \n')
				f.write('\t\"model\" : \"arcsecond.ObservingSite\", \n')
				f.write('\t\"fields\" : {\n')
				f.write('\t\t\"name\": \"'+name+'\",\n')
				f.write('\t\t\"IAUCode\": \"'+code+'\",\n')
				f.write('\t\t\"sources\": [\"MPC\"],\n')
				f.write('\t\t\"coordinates\": '+str(index)+'\n')
				f.write('\t}\n')
				f.write('},\n')
				
				index += 1
				
	f.write(']\n')
	
	
print '\n\n\n*** DO NOT FORGET TO REMOVE LAST comma!***\n\n\n'



# DOC
# The observatory codes are obtained from:
# 
# The Minor Planet Center: http://cfa-www.harvard.edu/iau/lists/ObsCodes.html presents the obs code, longitude, parallax constants (C=rho sin phi' and S=rho cos phi').
# A personal Web page: http://homepages.compuserve.de/Hdd74/code/CODE-MAP.HTM presents obs code, geodetic longitude, geodetic latitude, observatory name and the geocentric latitude
# There are 2 types of latitude and longitude:
# geocentric longitude, latitude and radius (lambda, phi', rho)
# geodetic longitude, latitude and elevation or height (lambda, phi, h)
# The former is needed for precise astronomical computations such as astrometric measurement and parallax, and is referenced to the true center of the earth. The latter system is a reference frame on the earth, and is used in maps, but can be off by as much as an arcmin from the geocentric system because of the flattened shape of the Earth.
# There is a detailed explanation in section K of the Astronomical Almanac for the reduction of terrestrial coordinate systems. The Geocentric coordinates may be calculated directly from geodetic coordinates, but an iterative procedure must be used for the inverse calculation.
# 
# The MPC web page is probably the most accurate and gets regularly updated. To compute the geocentric latitude from the parallax constants in the MPC:
# 
# phi' = atan(S/C) where S=rho cos phi' C=rho sin phi'
# 
