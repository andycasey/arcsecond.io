from django.conf import settings
from django.db import models
from django.utils import timezone

from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

import hashlib

class UserProfile(models.Model):
    class Meta: app_label = 'arcsecond'

    membership_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    def _email_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
    email_verified = property(_email_verified)

    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())


