from django import forms
from .models import SecondModel

class SecondModelForm(forms.ModelForm):
    class Meta:
        model = SecondModel
        fields = ['title', 'description', 'file']
