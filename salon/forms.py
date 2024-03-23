from django import forms
from django.utils import timezone
from datetime import time
from .models import Programare
from django.core.exceptions import ValidationError
from django.forms import DateInput, TimeInput


class ProgramareForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        ora = cleaned_data.get('ora')
        serviciu = cleaned_data.get('serviciu')

        # Verifică dacă există deja o programare confirmată pentru aceeași dată, oră și serviciu
        if Programare.objects.filter(data=data, ora=ora, serviciu=serviciu, confirmat=True).exists():
            raise ValidationError('Această dată și oră sunt deja rezervate pentru serviciul selectat. Te rugăm să alegi o altă opțiune.')

        return cleaned_data

    class Meta:
        model = Programare
        fields = ['nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'content']
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
            'ora': TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProgramareForm, self).__init__(*args, **kwargs)
        self.fields['data'].widget.attrs['min'] = timezone.localdate().isoformat()
        self.fields['ora'].widget.attrs['min'] = time(hour=9).isoformat()  # Ajustează conform programului tău
        self.fields['ora'].widget.attrs['max'] = time(hour=18).isoformat()  # Ajustează conform programului tău
