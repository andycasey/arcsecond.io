# -*- coding: utf-8 -*-

from defaults import *

DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.arcsecond.io',
    'arcsecond-prod.herokuapp.com'
]

SITE_ID = 2  # Local=1, Staging=1, Prod=2

