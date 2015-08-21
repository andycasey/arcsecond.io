__author__ = 'onekiloparsec'

from django.utils.translation import ugettext_lazy as _
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.sites.models import Site
from django.conf import settings

from meta.views import Meta

def get_generic_meta(title=None, url=None):
    # favicon_image_url = static('arcsecond/img/favicon-120.png')
    telescopes_image_url = static('arcsecond/img/screen-bg_11.jpg')
    site_domain = Site.objects.get_current().domain

    meta = Meta(
        description=_("arcsecond.io aims to provide unified REST APIs for astronomical information."),
        keywords=['data', 'astronomy', 'astrophysics', 'bigdata', 'json', 'REST', 'API', 'integration'],
        url='http://www.arcsecond.io',
        site_name='arcsecond.io',
        use_og=True,
        use_twitter=True,
        twitter_creator="@onekiloparsec",
        twitter_site="@arcsecond_io",
        twitter_card="summary_large_image",
        image="http://{0}{1}".format(site_domain, telescopes_image_url),
    )

    if title is not None:
        meta.title = title
    if url is not None:
        meta.url = url

    if settings.SITE_ID == 3: # PROD
        facebook_app_id = '884448981631297'
        meta.extra_custom_props = [('property','fb:app_id',facebook_app_id),]

    return meta

