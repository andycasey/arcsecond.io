
# See https://docs.djangoproject.com/en/1.7/ref/applications/
# Do not import any models here.

from django.apps import AppConfig
from allauth.account.signals import user_signed_up
from .signals import *

class ArcsecondIOAppConfig(AppConfig):
    name = 'project.arcsecond'
    verbose_name = "arcsecond.io"

    def ready(self):
        user_signed_up.connect(process_upon_user_signed_up, dispatch_uid="process_upon_user_signed_up")
