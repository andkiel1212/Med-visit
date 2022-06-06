from django import forms
from django.forms import ModelForm
from .models import Patient

class Search_form(forms.Form):
    query = forms.CharField
  

class CreatePatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
