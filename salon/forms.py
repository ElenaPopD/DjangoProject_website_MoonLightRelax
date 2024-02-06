from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subiect = forms.CharField()
    mesaj = forms.CharField(widget=forms.Textarea())

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        subiect = cleaned_data.get("subiect")
        mesaj = cleaned_data.get("mesaj")