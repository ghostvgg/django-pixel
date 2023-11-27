from django import forms

class CompoundInterestForm(forms.Form):
    principal = forms.IntegerField()
    year = forms.IntegerField()
    monthlyAmt = forms.IntegerField()
    apr = forms.FloatField()
