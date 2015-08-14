"""
Django settings for arcsecond project.

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
SITE_ID = 1  # Local=1, Staging=2, Prod=3

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

EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SERVER_EMAIL = "cedric@arcsecond.io"
DEFAULT_FROM_EMAIL = "cedric@arcsecond.io"

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
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
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
    'django_hosts',
    'leaflet',
    'multiselectfield',
    'corsheaders',
    'rest_framework_swagger',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.facebook',
    'project.arcsecond',
)

MIDDLEWARE_CLASSES = (
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
)

ROOT_URLCONF = 'project.arcsecond.urls_www'
ROOT_HOSTCONF = 'project.arcsecond.hosts'
DEFAULT_HOST = 'www'

WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows. Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

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

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(ROOT_PATH, 'components')
BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
    'bootstrap-social',
    'bootstrap-select',
    'angular',
    'angular-route',
    'angular-resource'
)

# https://github.com/sunlightlabs/django-honeypot
HONEYPOT_FIELD_NAME = 'oh_really_you_are_a_human'

INSTALLED_APPS += ('django_nose',)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=project.arcsecond.forms,project.arcsecond.models,project.arcsecond.views',
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
                'django.core.context_processors.i18n',

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

ACCOUNT_AUTHENTICATION_METHOD = "email"

# Used by django-allauth. No need to call url resolver 'reverse'.
LOGIN_URL = 'account_login'
# LOGIN_REDIRECT_URL = 'picolegends:user-profile-edit'

# django-allauth
# The URL to redirect to after a successful e-mail confirmation, in case no user is logged in
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
# The URL to redirect to after a successful e-mail confirmation, in case of an authenticated user.
# Set to None to use settings.LOGIN_REDIRECT_URL.
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True
# An integer specifying the minimum password length.
ACCOUNT_PASSWORD_MIN_LENGTH = 10

CORS_ORIGIN_WHITELIST = (
    'www.arcsecond.io',
    'api.arcsecond.io'
)

CORS_URLS_REGEX = r'^/docs/.*$'

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'base_path':'www.arcsecond.io/docs',
    'info': {
        'contact': 'cedric@onekilopars.ec',
        'description': 'This is the alpha version of arcsecond.io APIs.',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'termsOfServiceUrl': 'http://www.arcsecond.io/terms/',
        'title': 'arcsecond.io Swagger App',
    },
    'doc_expansion': 'none'
}
