from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
    # name = forms.CharField()
    class Meta:
        model = MyModel
        fields = ['img']