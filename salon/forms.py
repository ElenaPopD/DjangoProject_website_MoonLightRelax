from django import forms
from django.forms import ValidationError  # noqa: F401

from .models import Programare 

class ProgramareForm(forms.ModelForm):
    class Meta:
        model = Programare
        fields = ['nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'content']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'ora': forms.TimeInput(attrs={'type': 'time'}),
        }