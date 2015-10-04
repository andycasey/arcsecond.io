__author__ = 'onekiloparsec'

from django.utils.translation import ugettext_lazy as _
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.sites.models import Site
from django.conf import settings

from meta.views import Meta

def get_generic_meta(title=None, url=None, api=False):
    image_filename = 'screen-bg_11.jpg' if api is False else 'screen-bg_10.jpg'
    image_url = static('arcsecond/img/'+image_filename)

    meta = Meta(
        keywords=['astronomy', 'astrophysics', 'cloud', 'data', 'bigdata', 'REST', 'API', 'integration', 'sun', 'moon',
                  'sky', 'planets', 'exoplanets', 'earth', 'observing sites', 'telescopes'],

        description=_("The astronomy cloud."),
        url='http://www.arcsecond.io',
        site_name='arcsecond.io',
        use_og=True,
        use_twitter=True,
        twitter_creator="@onekiloparsec",
        twitter_site="@arcsecond_io",
        twitter_card="summary_large_image",

        image="http://www.arcsecond.io{0}".format(image_url),
    )

    if title is not None:
        meta.title = title
    if url is not None:
        meta.url = url

    if settings.SITE_ID == 3: # PROD
        facebook_app_id = '884448981631297'
        meta.extra_custom_props = [('property','fb:app_id',facebook_app_id),]

    return meta

