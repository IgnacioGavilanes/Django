from django.forms import ModelForm
from django import forms


class ContactForm (forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-email'}))
    message = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-message'}))