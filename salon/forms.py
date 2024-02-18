from django import forms
from django.utils import timezone
from datetime import time
from .models import Programare

class ProgramareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProgramareForm, self).__init__(*args, **kwargs)
        # Setează data minimă la data curentă și ora minimă la ora deschiderii (exemplu: 09:00 AM)
        self.fields['data'].widget.attrs['min'] = timezone.localdate().isoformat()
        self.fields['ora'].widget.attrs['min'] = time(hour=9).isoformat()  # Ora de început a programului de lucru
        self.fields['ora'].widget.attrs['max'] = time(hour=18).isoformat()  # Ora de sfârșit a programului de lucru

    class Meta:
        model = Programare  
        fields = ['nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'content']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'ora': forms.TimeInput(attrs={'type': 'time'}),
        }
