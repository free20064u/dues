from django import forms
from django.db import models
from .models import *
from main.models import Program


class FileForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(),empty_label='Select Program', widget=forms.Select(attrs={'class':'form-control border border-primary rounded'}))
    file = forms.FileField(label='Excel file', widget=forms.FileInput(attrs={'class':'form-control border border-primary rounded'}))
    class Meta:
        model=File
        fields = '__all__'
