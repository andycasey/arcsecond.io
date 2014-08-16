
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Represent all the information associated with a user/author that must be added to the
    basic :model:`auth.User` class, which is kept as is for auth purposes only.
    """
    user = models.OneToOneField(User, related_name="profile")

    def __unicode__(self):
        try:
            return "UserProfile (user: "+self.user.get_username()+")"
        except User.DoesNotExist:
            return "UserProfile (no user set)"
