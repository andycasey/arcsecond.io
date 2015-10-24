# -*- coding: utf-8 -*-

from defaults import *

DEBUG = False

INSTALLED_APPS += (
    'opbeat.contrib.django',
)

OPBEAT = {
    'ORGANIZATION_ID': '29db67b358ce4dd5876cce447b379ea5',
    'APP_ID': '2bf4080a15',
    'SECRET_TOKEN': 'f9ce3e383470db99b4ad0ccf7db653066c72b80b',
}

# The ending comma is crucial
MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
) + MIDDLEWARE_CLASSES

ALLOWED_HOSTS = [
    '.arcsecond.io',
    'arcsecond-prod.herokuapp.com'
]

SITE_ID = 3  # Local=1, Staging=2, Prod=3

CORS_ORIGIN_ALLOW_ALL = True
CSRF_COOKIE_DOMAIN = ".arcsecond.io"

# CORS_ORIGIN_WHITELIST = (
#     'arcsecond.io',
# )

ARCSECOND_API_ROOT_URL = "//api.arcsecond.io"
PARENT_HOST = "arcsecond.io"

ACCOUNT_PASSWORD_MIN_LENGTH = 10
