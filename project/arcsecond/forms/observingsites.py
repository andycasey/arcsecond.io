from django import forms
from project.arcsecond.models import ObservingSite


class ObservingSiteForm(forms.ModelForm):
    class Meta:
        model = ObservingSite
        fields = ['short_name', 'name', 'alternate_name_1', 'alternate_name_2', 'IAUCode', 'continent', 'country', 'coordinates']
