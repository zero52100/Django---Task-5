from django import forms
from .models import FirstModel

class FirstModelForm(forms.ModelForm):
    class Meta:
        model = FirstModel
        fields = ['name', 'age', 'email']
