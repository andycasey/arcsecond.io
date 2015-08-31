#!/Users/onekiloparsec/.virtualenvs/iobs-debug/bin/python
# -*- coding: utf-8 -*-

__author__ = 'onekiloparsec'

import os
import plistlib as plist
import json
from datetime import datetime
import sys
sys.path.append("..")
from project.arcsecond.models.observingsites import *

class ObservingSitesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

def get_source_path():
    return os.path.join(os.path.expanduser("~"), 'Apps', 'iObserve1', 'Observatories')

def get_clean_obs_name(observatory_name):
    clean_obs_name = observatory_name.lower().replace(' ', '').replace('/', '')
    clean_obs_name = clean_obs_name.replace(u'ó', u'o').replace('.', '').replace(u'á', 'a').replace(u'ü', 'u')
    clean_obs_name = clean_obs_name.replace(u'ç', 'c').replace(u'é', u'e').replace(u'è', u'e')
    return clean_obs_name

def get_obervatory_property_file(observatory_name):
    clean_obs_name = get_clean_obs_name(observatory_name)
    return os.path.join(get_source_path(), 'Properties', clean_obs_name+'.plist')

def get_fixtures_file_path(continent_name, suffix):
    fixtures_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'project', 'arcsecond', 'fixtures')
    fixture_file_path = os.path.join(fixtures_dir, continent_name.lower().replace(' ', '_')) + '_'+suffix+'.json'
    return fixture_file_path

def get_observatory_names(continent_name):
    source_path = get_source_path()
    obs_list_file = os.path.join(source_path, 'ObservatoryLists.plist')
    obs_list_plist = plist.readPlist(obs_list_file)
    return obs_list_plist[continent_name]


def create_observing_site_fixtures():
    continent_keys = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
    for continent_key in continent_keys:
        observatory_names = get_observatory_names(continent_key)
        fixture_file_path = get_fixtures_file_path(continent_key, 'observing_sites')
        print fixture_file_path

        f = open(fixture_file_path, 'w')
        f.write('[\n')

        for observatory_name in observatory_names:
            if u'→' in observatory_name: continue
            print u' • ' + observatory_name
            obs_file = get_obervatory_property_file(observatory_name)

            if not os.path.exists(obs_file):
                print '*** NOT FOUND', obs_file
                # raise Exception
                continue

            obs_plist = plist.readPlist(obs_file)
            obs = obs_plist['observatory'] if obs_plist.has_key('observatory') else obs_plist
            coords = obs['coordinates']
            longitude = coords['longitude']
            latitude = coords['latitude']

            longitude_sign = 1.0
            if float(longitude[0]) < 0 or float(longitude[1]) < 0 or float(longitude[2]) < 0:
                longitude_sign = -1.0

            latitude_sign = 1.0
            if float(latitude[0]) < 0 or float(latitude[1]) < 0 or float(latitude[2]) < 0:
                latitude_sign = -1.0

            longitude_value = longitude_sign * (abs(longitude[0]) + abs(longitude[1])/ 60.0 + abs(longitude[2])/3600.0)
            latitude_value = latitude_sign * (abs(latitude[0]) + abs(latitude[1])/ 60.0 + abs(latitude[2])/3600.0)

            coordinates = {'model': 'arcsecond.Coordinates', 'pk': None}
            coordinates['fields'] = { 'longitude': longitude_value, 'latitude': latitude_value, 'height': coords['altitude'] }

            observing_site = {'model': 'arcsecond.ObservingSite', 'pk': None}
            observing_site['fields'] = {
                'name': obs['name'],
                'long_name': obs['longName'],
                'IAUCode': obs['IAUCode'] if obs.has_key('IAUCode') else "",
                'coordinates': [longitude_value, latitude_value],
                'continent': continent_key,
                'country': obs['country'],
                'time_zone': obs['timeZone'],
                'time_zone_name': obs['timeZoneName']
            }

            if obs['websites'].has_key('main'):
                observing_site['fields']['homepage'] = obs['websites']['main']
            if obs['websites'].has_key('wikipedia-en'):
                observing_site['fields']['wikipedia_article'] = obs['websites']['wikipedia-en']

            f.write(json.dumps(coordinates, indent=4))
            f.write(',\n')
            f.write(json.dumps(observing_site, indent=4))

            if observatory_name != observatory_names[-1]:
                f.write(',\n')

        f.write('\n]')
        f.close()

def create_telescope_fixtures():
    continent_keys = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
    for continent_key in continent_keys:
        observatory_names = get_observatory_names(continent_key)
        fixture_file_path = get_fixtures_file_path(continent_key, 'telescopes')
        print fixture_file_path

        f = open(fixture_file_path, 'w')
        f.write('[\n')

        for observatory_name in observatory_names:
            if u'→' in observatory_name: continue
            print u' • ' + observatory_name
            obs_file = get_obervatory_property_file(observatory_name)

            if not os.path.exists(obs_file):
                print '*** NOT FOUND', obs_file
                # raise Exception
                continue

            obs_plist = plist.readPlist(obs_file)
            obs = obs_plist['observatory'] if obs_plist.has_key('observatory') else obs_plist

            if obs['observingTools']:
                for tool in obs['observingTools']:
                    if tool['class'] == 'OpticalTelescope':
                        tel = tool['telescope']
                        tel_name = tool['observingTool']['longName']

                        print tel

                        dome = {'model': 'arcsecond.Dome', 'pk': None}
                        dome_name = tel_name+' Dome'
                        dome['fields'] = { 'name': dome_name }

                        telescope = {'model':'arcsecond.Telescope', 'pk': None}
                        telescope['fields'] = {
                            'dome': dome_name,
                            'name': tel_name
                        }

                        if 'mounting' in tel['mounting']:
                            if tel['mounting'].lower() in ['cassegrain',]:
                                telescope['fields']['mounting'] = Telescope.MOUNTING_CASSEGRAIN
                            elif tel['mounting'].lower() in ['equatorial',]:
                                telescope['fields']['mounting'] = Telescope.MOUNTING_EQUATORIAL
                            elif tel['mounting'].lower() in ['alt-az', 'alt-azimuth']:
                                telescope['fields']['mounting'] = Telescope.MOUNTING_ALTAZ
                            elif tel['mounting'].lower() in ['off-axis']:
                                telescope['fields']['mounting'] = Telescope.MOUNTING_OFF_AXIS

                        if 'opticalDesign' in tel:
                            if tel['opticalDesign'].lower() in [u'ritchey-chrétien',]:
                                telescope['fields']['optical_design'] = Telescope.OPTICAL_DESIGN_RITCHEY_CHRETIEN
                            elif tel['opticalDesign'].lower() in [u'schmidt',]:
                                telescope['fields']['optical_design'] = Telescope.OPTICAL_DESIGN_SCHMIDT

                        mirror = None
                        if 'primaryMirror' in tel:
                            mirror = {'model':'arcsecond.Mirror', 'pk': None}
                            mirror['fields'] = {
                                'mirror_index': 0,
                                'telescope': tel_name,
                                'diameter': float(tel['primaryMirror']['diameter'])
                            }

                        if 'hasAdaptativeOptics' in tel:
                            telescope['fields']['has_active_optics'] = True if tel['hasAdaptativeOptics'] == 'YES' else False
                        if 'hasActiveOptics' in tel:
                            telescope['fields']['has_adaptative_optics'] = True if tel['hasActiveOptics'] == 'YES' else False
                        if 'hasLaserGuideStar' in tel:
                            telescope['fields']['has_laser_guide_star'] = True if tel['hasLaserGuideStar'] == 'YES' else False

                        f.write(json.dumps(dome, indent=4))
                        f.write(',\n')
                        if mirror is not None:
                            f.write(json.dumps(mirror, indent=4))
                            f.write(',\n')
                        f.write(json.dumps(telescope, indent=4))
                        f.write(',\n')

            if observatory_name != observatory_names[-1]:
                f.write(',\n')

        f.write('\n]')
        f.close()


if __name__ == '__main__':
    create_observing_site_fixtures()
    create_telescope_fixtures()
