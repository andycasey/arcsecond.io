# -*- coding: utf-8 -*-

from defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BROKER_POOL_LIMIT = 1

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

PARENT_HOST = "lvho.st:8000"
