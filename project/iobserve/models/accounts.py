
from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings
#
class UserProfile(models.Model):
    """
    Represent all the information associated with a user/author that must be added to the
    basic :model:`auth.User` class, which is kept as is for auth purposes only.
    """
    class Meta: app_label = 'iobserve'

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="profile", primary_key=True)

    # def __unicode__(self):
#         try:
#             return "UserProfile (user: "+self.user.get_username()+")"
#         except get_user_model().DoesNotExist:
#             return "UserProfile (no user set)"
