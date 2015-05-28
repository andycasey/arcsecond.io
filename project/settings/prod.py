# -*- coding: utf-8 -*-

from defaults import *

DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.eclipt.is',
    'iobserve-server.herokuapp.com'
]

SITE_ID = 1  # Local=1, Staging=1, Prod=2

