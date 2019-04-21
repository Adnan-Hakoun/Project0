from django import forms
from .models import Maker



class Add_maker(forms.ModelForm):
    class Meta():
        model=Maker
        fields=['title','nationality']
