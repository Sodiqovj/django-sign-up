from dataclasses import fields
from django import forms
from .models import *


class Login(forms.ModelForm):
    class Meta:
        model = My
        fields = (
            'name',
            'name2',
            'email'
        )