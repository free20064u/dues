from django import forms
from django.db import models
from accounts.models import CustomUser

from .models import Student, Program, Credit, Message


class ProgramForm(forms.ModelForm):
    program_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Program name'}))
    short_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Program short name'}))
    amount = forms.DecimalField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Amount'}))
    
    class Meta:
        model = Program
        fields = ['program_name','short_name','amount']


class StudentForm(forms.ModelForm):
    image = forms.ImageField(label='', widget= forms.FileInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    program = forms.ModelChoiceField(label='', queryset=Program.objects.all(), widget=forms.Select(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    
    class Meta:
        model = Student
        fields = ['image', 'first_name', 'middle_name', 'last_name','program']


class CreditForm(forms.ModelForm):
    student = forms.ModelChoiceField(label='', queryset=Student.objects.all(), widget = forms.TextInput(attrs={'type':'hidden'}))
    amount = forms.DecimalField(label='', widget = forms.TextInput(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Amount'}))
    edited_by = forms.ModelChoiceField(label='', queryset=CustomUser.objects.all(), widget = forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = Credit
        fields = ['student', 'amount', 'edited_by']


class MessageForm(forms.ModelForm):
    title = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Title'}))
    description = forms.Textarea(attrs={'class':'form-control mb-2 border border-primary'})
    class Meta:
        model = Message
        fields = ['title', 'description']