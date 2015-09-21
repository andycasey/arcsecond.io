# -*- coding: utf-8 -*-

from defaults import *

DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BROKER_POOL_LIMIT = 1

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Amazing trick: http://stackoverflow.com/questions/7335680/subdomain-on-localhost
ARCSECOND_API_ROOT_URL = "http://api.lvho.st:8000"
PARENT_HOST = "lvho.st:8000"


