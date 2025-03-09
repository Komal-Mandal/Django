from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    roll = forms.IntegerField()
    city = forms.CharField()