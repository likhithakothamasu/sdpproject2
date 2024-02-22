from django import forms

class IntegerDateForm(forms.Form):
    integer_value = forms.IntegerField()
    date_value = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
