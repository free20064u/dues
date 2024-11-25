from django import forms
from django.db import models
from .models import *
from main.models import Program


class FileForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    class Meta:
        model=File
        fields = '__all__'
