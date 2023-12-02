from django import forms

class PredictionForm(forms.Form):
    feature1 = forms.CharField(label='Feature 1')
    feature2 = forms.CharField(label='Feature 2')
    feature3 = forms.CharField(label='Feature 3')
    feature4 = forms.CharField(label='Feature 4')