"""
Django settings for iobserve project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Absolute path of the whole project "PicoLegends-Django" root directory.
ROOT_PATH = os.path.dirname(PROJECT_PATH)

ADMINS = (('Cedric', 'cedric@onekilopars.ec'), )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
SITE_ID = 1  # Local=1, Staging=1, Prod=2

# Internationalization
from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
)

LOCALE_PATH = os.path.join(os.path.join(ROOT_PATH, 'conf'), "locale")
LOCALE_PATHS = (
    LOCALE_PATH,
)

# https://docs.djangoproject.com/en/1.6/topics/i18n/
# If the locale middleware isn't in use, it decides which translation is served to all users
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'UTC'
USE_TZ = True

from ..utils import get_env_variable
# Will look in os.environ first, and if None is returned, will look at .env file.

SECRET_KEY = get_env_variable('SECRET_KEY')
DATABASE_URL = get_env_variable('DATABASE_URL')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'mptt',
    'djangobower',
    'honeypot',
    'leaflet',
    'multiselectfield',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    'project.iobserve',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows. Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

# See https://github.com/jakubroztocil/django-settings-export
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django_settings_export.settings_export',
    'django.template.context_processors.i18n'
]

SETTINGS_EXPORT = [
    'DEBUG',
    'SITE_ID',
]

import dj_database_url
DATABASES = { 'default': dj_database_url.config(default=os.environ['DATABASE_URL']) }

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(ROOT_PATH, 'components')
BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
    'bootstrap',
    'fontawesome',
    'prettify',
)

# https://github.com/sunlightlabs/django-honeypot
HONEYPOT_FIELD_NAME = 'oh_really_you_are_a_human'

INSTALLED_APPS += ('django_nose',)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=project.iobserve.forms,project.iobserve.models,project.iobserve.views',
]


LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (0.0, 0.0),
    'DEFAULT_ZOOM': 2,
    'MIN_ZOOM': 2,
    'MAX_ZOOM': 18,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django_settings_export.settings_export',

                # `allauth` needs this from django
                'django.template.context_processors.request',

                # `allauth` specific context processors
                'allauth.account.context_processors.account',
                'allauth.socialaccount.context_processors.socialaccount',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
