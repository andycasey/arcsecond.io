__author__ = 'onekiloparsec'

from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'api', 'urls_api', name='api'),
    host(r'www', 'urls_www', name='www'),
)
