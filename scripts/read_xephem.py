#!/usr/bin/env python

with open('../project/arcsecond/fixtures/xephem.json', 'w') as f:
	f.write('[\n')
	
	with open('xephem_sites.txt', 'r') as x:
		lines = x.readlines()
		index = 1000
		
		for line in lines:
			if len(line.strip()) > 0 and line[0] != '#' and line[:3] != '---':
				name_country, latitude, longitude, height, time_zone = line.split(';')
				name_country_elements = name_country.split(',')
				
				latitude_elements = [ el.strip() for el in latitude.split(' ') if len(el.strip()) > 0 ]
				longitude_elements = [ el.strip() for el in longitude.split(' ') if len(el.strip()) > 0 ]
				
				name = name_country_elements[0].strip()
				country = name_country_elements[-1].strip() if len(name_country_elements) > 1 else '?'
				state = name_country_elements[1].strip() if len(name_country_elements) == 3 else ''
								
				latitude = float(latitude_elements[0]) + float(latitude_elements[1])/60.0 + float(latitude_elements[2])/360.0
				if latitude_elements[-1] == 'S':
					latitude = -1*latitude;

				longitude = float(longitude_elements[0]) + float(longitude_elements[1])/60.0 + float(longitude_elements[2])/360.0
				if longitude_elements[-1] == 'W':
					longitude = -1*longitude;
					
				print 80*'-'
				print '*', name
				print '('+state+')', country, '['+time_zone.strip()+']'
				print longitude, latitude, height.strip()
				
				f.write('{\n')
				f.write('\t\"pk\" : '+str(index)+', \n')
				f.write('\t\"model\" : \"arcsecond.Coordinates\", \n')
				f.write('\t\"fields\" : {\n')
				f.write('\t\t\"latitude\": '+str(latitude)+',\n')
				f.write('\t\t\"longitude\": '+str(longitude)+',\n')
				f.write('\t\t\"height\": '+str(float(height.strip()))+'\n')
				f.write('\t}\n')
				f.write('},\n')

				f.write('{\n')
				f.write('\t\"pk\" : '+str(index)+', \n')
				f.write('\t\"model\" : \"arcsecond.ObservingSite\", \n')
				f.write('\t\"fields\" : {\n')
				f.write('\t\t\"name\": \"'+name+'\",\n')
				f.write('\t\t\"state_province\": \"'+state+'\",\n')
				f.write('\t\t\"country\": \"'+country+'\",\n')
				f.write('\t\t\"sources\": [\"Xephem\"],\n')
				f.write('\t\t\"coordinates\": '+str(index)+'\n')
				f.write('\t}\n')
				f.write('},\n')
				
				index += 1
				
	f.write(']\n')
	
	
print '\n\n\n*** DO NOT FORGET TO REMOVE LAST comma!***\n\n\n'