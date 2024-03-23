from django import forms
from django.utils import timezone
from datetime import time

from .models import Programare
from django.core.exceptions import ValidationError
from django.forms import DateInput, TimeInput

class ProgramareForm(forms.ModelForm):
    # Generează opțiunile de oră (de la 09:00 la 18:00, de exemplu)
    ORA_CHOICES = [(time(hour=h, minute=m).strftime('%H:%M'), time(hour=h, minute=m).strftime('%H:%M')) 
    for h in range(9, 20) for m in (0, 45)]
    
    ora = forms.ChoiceField(choices=ORA_CHOICES, widget=forms.Select(), label="Ora")
    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        ora = cleaned_data.get('ora')
        serviciu = cleaned_data.get('serviciu')

        # Verifică dacă există deja o programare confirmată pentru aceeași dată, oră și serviciu
        if Programare.objects.filter(data=data, ora=ora, serviciu=serviciu, confirmat=True).exists():
            raise ValidationError("Această dată și oră sunt deja rezervate pentru serviciul selectat.\nTe rugăm să alegi o altă opțiune.")

        return cleaned_data

    class Meta:
        model = Programare
        fields = ['nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'observatii']
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProgramareForm, self).__init__(*args, **kwargs)
        self.fields['data'].widget.attrs['min'] = timezone.localdate().isoformat()



