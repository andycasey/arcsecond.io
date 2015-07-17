__author__ = 'onekiloparsec'

from django import template
from django.utils.timesince import timesince
from django.utils.translation import ugettext_lazy as _

import datetime
import pytz

register = template.Library()

@register.filter
def better_timesince(value):
    if value is None:
        return ""
    result = timesince(value, now=datetime.datetime.now(pytz.utc))
    if result.strip() == "0 minutes":
        return _("just now")
    return _("%s ago")%(result)
