from django import forms
from ..models import UserProfile

import re

def check_valid_ascii_string(s, search=re.compile(r'[^a-zA-Z0-9.]').search):
    return not bool(search(s))

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username =  forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email')

    # def save(self, *args, **kw):
    #     kw['commit'] = False
    #     profile = super(UserProfileForm, self).save(*args, **kw)
    #     profile.user = self.user
    #     profile.save()
    #
    #
