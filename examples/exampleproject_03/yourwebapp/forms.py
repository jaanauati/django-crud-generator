from django import forms
from yourwebapp.models import YourModel

class YourModelModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
    extrafield = forms.CharField(label="Extra field for YourModel")

