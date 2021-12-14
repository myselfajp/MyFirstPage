from django import forms
from Blog.models import comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = '__all__'