from django import forms
from django.db import models
from .models import *
from main.models import Program


class GFGForm(forms.ModelForm):
    class Meta:
        model= GFG
        fields ='__all__'


class FileForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    class Meta:
        model=File
        fields = '__all__'
