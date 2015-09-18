__author__ = 'onekiloparsec'

from django_hosts import patterns, host

host_patterns = patterns('project.arcsecond',
    host(r'www', 'urls_www', name='www'),
    host(r'api', 'urls_api', name='api'),
)
