from django import forms

from denguealert.models import DengueCase


class DengueCaseForm(forms.ModelForm):
    class Meta:
        model = DengueCase
        fields = ['patient_name', 'onset_date']


class DengueCaseLocationForm(forms.ModelForm):
    class Meta:
        model = DengueCaseLocation
        fields = ['name', 'address', 'latitude', 'longitude']

    latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'true'}))
    longitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'true'}))
