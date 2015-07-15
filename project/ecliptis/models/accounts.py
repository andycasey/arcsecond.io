from django.conf import settings
from django.db import models

from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

import hashlib

class UserProfile(models.Model):
    class Meta:
        db_table = 'user_profile'
        app_label = 'ecliptis'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())


