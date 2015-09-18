# -*- coding: utf-8 -*-

from defaults import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.arcsecond.io',
    'arcsecond-prod.herokuapp.com'
]

SITE_ID = 3  # Local=1, Staging=2, Prod=3

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'www.arcsecond.io',
    'api.arcsecond.io'
)

ARCSECOND_API_ROOT_URL = "http://api.arcsecond.io"
PARENT_HOST = "arcsecond.io"

