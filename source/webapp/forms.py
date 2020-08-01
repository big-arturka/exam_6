from django import forms


class EntryForm(forms.Form):
    author = forms.CharField(max_length=100, required=True, label='Автор:',
                             widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(max_length=100, required=True, label='Email:',
                             widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=2000, required=True, label='Отзыв:',
                                  widget=forms.Textarea(attrs={'class': 'form-area'}))
