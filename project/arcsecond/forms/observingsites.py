from django import forms
from project.arcsecond.models import ObservingSite


class ObservingSiteForm(forms.ModelForm):
    class Meta:
        model = ObservingSite
        fields = ['name', 'long_name', 'IAUCode', 'continent', 'coordinates']
