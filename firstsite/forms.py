from django import forms
from django.forms.widgets import Textarea
from firstsite.models import Contact,NewsLetter

# class NameForm(forms.Form):
#     name=forms.CharField(max_length=255)
#     email=forms.EmailField()
#     subject=forms.CharField(max_length=255)
#     message= forms.CharField(widget=Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields ='__all__'