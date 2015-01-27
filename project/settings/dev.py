# -*- coding: utf-8 -*-

from defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BROKER_POOL_LIMIT = 1

SITE_ID = 0  # Local=0, Staging=1, Prod=2
