__author__ = 'onekiloparsec'

from django import template
from django.contrib.sites.models import Site

register = template.Library()

@register.simple_tag(takes_context=True)
def site_domain(context): # Template takes at least one argument...
    """Returns the URL of the default site.
    :rtype : str
    """
    try:
        return Site.objects.get_current().domain
    except Site.DoesNotExist:
        return None

