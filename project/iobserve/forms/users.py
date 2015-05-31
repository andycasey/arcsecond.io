from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from ..models import UserProfile, UserSettings

# from tinymce.widgets import TinyMCE

import re

def check_valid_ascii_string(s, search=re.compile(r'[^a-zA-Z0-9.]').search):
    return not bool(search(s))

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email')

    def save(self, *args, **kw):
        kw['commit'] = False
        profile = super(UserProfileForm, self).save(*args, **kw)
        profile.user = self.user
        profile.save()



class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings

    def __init__(self, user, *args, **kwargs):
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        self.user = user

