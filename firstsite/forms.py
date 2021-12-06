from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Textarea

class NameForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    message= forms.CharField(widget=Textarea)
