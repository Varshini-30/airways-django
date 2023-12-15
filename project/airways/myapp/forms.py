from django import forms
from .models import log


class login(forms.ModelForm):
    class Meta:
        model = log
        fields = ('name', 'email', 'phone')


class SearchForm(forms.Form):
    q = forms.CharField(label='search', max_length=50)
