from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from main.models import Program


class UserRegisterForm(UserCreationForm):
    image = forms.ImageField(label='', widget= forms.FileInput(attrs={'class':'form-control mb-2 border border-primary'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Email'}))
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    password1 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Password'}))
    password2 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Password Confirm'}))
    class Meta:
        model = CustomUser
        fields = ['image','first_name', 'middle_name', 'last_name','username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Email'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','username', 'email']

class ProfileForm(forms.ModelForm):
    image = forms.ImageField(label='')

    class Meta:
        model = CustomUser
        fields = ['image', 'middle_name']
# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label='', widget= forms.FileInput(attrs={'class':'form-control mb-2 border border-primary'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    
    class Meta:
        model = CustomUser
        fields = ['image','first_name', 'middle_name', 'last_name']

class UserPrograUpdateForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all())
    class Meta:
        model= CustomUser
        fields = ['program']


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'class': 'form-control border border-primary', 'placeholder':'Password'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'password']