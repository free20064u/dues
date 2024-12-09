from django import forms
from django.db import models
from accounts.models import CustomUser

from .models import Student, Program, Credit, Message, TeacherCredit

# A form for adding pragrams 
class ProgramForm(forms.ModelForm):
    program_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Program name'}))
    short_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Program short name'}))
    amount = forms.DecimalField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Amount'}))
    
    class Meta:
        model = Program
        fields = ['program_name','short_name','amount']

# A Form for adding students
class StudentForm(forms.ModelForm):
    image = forms.ImageField(label='',required=False, widget= forms.FileInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='',required=False, widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    program = forms.ModelChoiceField(label='', queryset=Program.objects.all(),empty_label='Select program', widget=forms.Select(attrs={'class':'form-control mb-2 border border-primary'}))
    
    class Meta:
        model = Student
        fields = ['image', 'first_name', 'middle_name', 'last_name','program']

# A form for adding payment made by student
class CreditForm(forms.ModelForm):
    student = forms.ModelChoiceField(label='', queryset=Student.objects.all(), widget = forms.TextInput(attrs={'type':'hidden'}))
    amount = forms.DecimalField(label='', widget = forms.TextInput(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Amount'}))
    edited_by = forms.ModelChoiceField(label='', queryset=CustomUser.objects.all(), widget = forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = Credit
        fields = ['student', 'amount', 'edited_by']

# A form for sending messages to the admin
class MessageForm(forms.ModelForm):
    title = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Title'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control border border-primary', 'placeholder':'Message', 'rows':'6'}))
    class Meta:
        model = Message
        fields = ['title', 'description']

class TeacherCreditForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(label='', queryset=CustomUser.objects.all(), widget = forms.TextInput(attrs={'type':'hidden'}))
    amount = forms.DecimalField(label='', widget = forms.TextInput(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Amount'}))
    edited_by = forms.ModelChoiceField(label='', queryset=CustomUser.objects.all(), widget = forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = TeacherCredit
        fields = ['teacher', 'amount', 'edited_by']