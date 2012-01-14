from django import forms
from {{appname}}.models import {{modelname}}

class {{modelname}}ModelForm(forms.ModelForm):
    class Meta:
        model = {{modelname}}
    extrafield = forms.CharField(label="Extra field for {{modelname}}")

