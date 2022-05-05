from django import forms

class DateForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'id_start'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'id_end'}))