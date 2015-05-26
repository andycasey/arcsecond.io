#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'onekiloparsec'

import os
import sys
import plistlib as plist
import json
from datetime import datetime

class ObservingSitesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    source_path = os.path.join(os.path.expanduser("~"), 'Apps', 'iObserve', 'Observatories')
    obs_list_file = os.path.join(source_path, 'ObservatoryLists.plist')
    obs_list_plist = plist.readPlist(obs_list_file)
    fixtures_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'project', 'iobserve', 'fixtures')

    continent_keys = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
    for continent_key in continent_keys:
        observatory_names = obs_list_plist[continent_key]
        fixture_file = os.path.join(fixtures_dir, continent_key.lower().replace(' ', '_')) + '.json'
        print fixture_file

        f = open(fixture_file, 'w')
        f.write('[\n')

        for observatory_name in observatory_names:
            print '***' + observatory_name + '***'

            clean_obs_name = observatory_name.lower().replace(' ', '').replace('/', '')
            clean_obs_name = clean_obs_name.replace(u'ó', u'o').replace('.', '').replace(u'á', 'a').replace(u'ü', 'u')
            clean_obs_name = clean_obs_name.replace(u'ç', 'c').replace(u'é', u'e').replace(u'è', u'e')
            obs_file = os.path.join(source_path, 'Properties', clean_obs_name+'.plist')

            if not os.path.exists(obs_file):
                print obs_file
                raise Exception

            obs_plist = plist.readPlist(obs_file)
            obs = obs_plist['observatory'] if obs_plist.has_key('observatory') else obs_plist
            coords = obs['coordinates']
            longitude = coords['longitude']
            latitude = coords['latitude']

            longitude_sign = 1.0
            if float(longitude[0]) < 0 or float(longitude[1]) < 0 or float(longitude[2]) < 0:
                longitude_sign = -1.0;

            latitude_sign = 1.0
            if float(latitude[0]) < 0 or float(latitude[1]) < 0 or float(latitude[2]) < 0:
                latitude_sign = -1.0;

            longitude_value = longitude_sign * (abs(longitude[0]) + abs(longitude[1])/ 60.0 + abs(longitude[2])/3600.0)
            latitude_value = latitude_sign * (abs(latitude[0]) + abs(latitude[1])/ 60.0 + abs(latitude[2])/3600.0)

            coordinates = {'model': 'iobserve.Coordinates', 'pk': None}
            coordinates['fields'] = { 'longitude': longitude_value, 'latitude': latitude_value, 'height': coords['altitude'] }

            site = {'model': 'iobserve.Site', 'pk': None}
            site['fields'] = {
                'name': obs['name'],
                'long_name': obs['longName'],
                'coordinates': [longitude_value, latitude_value],
                'continent': continent_key,
                'country': obs['country'],
                'time_zone': obs['timeZone'],
                'time_zone_name': obs['timeZoneName']
            }

            if obs['websites'].has_key('main'):
                site['fields']['homepage'] = obs['websites']['main']
            if obs['websites'].has_key('wikipedia-en'):
                site['fields']['wikipedia_article'] = obs['websites']['wikipedia-en']

            observing_site = {'model': 'iobserve.ObservingSite', 'pk': obs['name']}
            observing_site['fields'] = { 'IAUCode': obs['IAUCode'] if obs.has_key('IAUCode') else "" }

            f.write(json.dumps(coordinates, indent=4))
            f.write(',\n')
            f.write(json.dumps(site, indent=4))
            f.write(',\n')
            f.write(json.dumps(observing_site, indent=4))

            if obs['observingTools']:
                for tool in obs['observingTools']:
                    if tool['class'] == 'OpticalTelescope':
                        tel = tool['telescope']

                        dome = {'model': 'iobserve.Dome', 'pk': None}
                        dome_name = tool['observingTool']['longName']+' Dome'
                        dome['fields'] = { 'name': dome_name}

                        telescope = {'model':'iobserve.Telescope', 'pk': None}
                        telescope['fields'] = {'dome': dome_name}

                        if 'mounting' in tel['mounting'] and tel['mounting'].lower() in ['cassegrain', 'equatorial']:
                            telescope['fields']['mounting'] = "cas" if tel['mounting'].lower() == 'cassegrain' else 'equ'

                        if 'opticalDesign' in tel and tel['opticalDesign'].lower() in [u'ritchey-chrétien', 'schmidt']:
                            telescope['fields']['optical_design'] = "rc" if tel['opticalDesign'].lower() == 'ritchey-chrétien' else 'sc'

                        # if 'primaryMirror' in tel:
                        #     mirror = {'model':'iobserve.Mirror', 'pk': None}


            if observatory_name != observatory_names[-1]:
                f.write(',\n')

        f.write('\n]')
        f.close()