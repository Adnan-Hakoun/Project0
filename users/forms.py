from django import forms
from django.contrib.auth.models import User


class Sign_in(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password']


class Sign_up(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password']
