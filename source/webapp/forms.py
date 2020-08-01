from django import forms
from .models import ENTRY_STATUS, DEFAULT_STATUS


class EntryForm(forms.Form):
    author = forms.CharField(max_length=100, required=True, label='Автор:',
                             widget=forms.TextInput(attrs={'class': 'form-input'}))

    email = forms.EmailField(max_length=100, required=True, label='Email:',
                             widget=forms.TextInput(attrs={'class': 'form-input'}))

    description = forms.CharField(max_length=2000, required=True, label='Отзыв:',
                                  widget=forms.Textarea(attrs={'class': 'form-area'}))

    status = forms.ChoiceField(choices=ENTRY_STATUS, label='Статус:', initial=DEFAULT_STATUS,
                               widget=forms.Select(attrs={'class': 'form-select'}))
