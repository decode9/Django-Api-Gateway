from django import forms

class VideogameValidation(forms.Form):
   name = forms.CharField(max_length=50)
   score = forms.FloatField()