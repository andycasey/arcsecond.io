# -*- coding: utf-8 -*-

from defaults import *

DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.onekilopars.ec',
    '.onekiloparsec.com',
    'iobserve-server.herokuapp.com'
]

SITE_ID = 2  # Local=0, Staging=1, Prod=2

