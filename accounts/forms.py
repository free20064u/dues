from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from .models import CustomUser
from main.models import Program

# A form for the registration of users 
class UserRegisterForm(UserCreationForm):
    image = forms.ImageField(label='',required=False, widget= forms.FileInput(attrs={'class':'form-control mb-2 border border-primary'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='',required=False, widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Email'}))
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    password1 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Password'}))
    password2 = forms.CharField(label='', widget= forms.PasswordInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Password Confirm'}))
    class Meta:
        model = CustomUser
        fields = ['image','first_name', 'middle_name', 'last_name','username', 'email', 'password1', 'password2']

# A form for updating user information by the users themselve
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='',required=False, widget=forms.EmailInput(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Email'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='',required=False, widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    class Meta:
        model = CustomUser
        fields = ['first_name','middle_name', 'last_name','username', 'email']

# A form for updating information about users by the administrator of the app
class AdminUserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='',required=False, widget=forms.EmailInput(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Email'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='',required=False, widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    program = forms.ModelMultipleChoiceField(label='',queryset=Program.objects.all(),widget=forms.SelectMultiple(attrs={'class':'form-control bb-2 border border-primary'}))
    
    class Meta:
        model = CustomUser
        fields = ['first_name','middle_name', 'last_name','username', 'email', 'program','is_superuser','is_active','is_staff']


# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label='',required=False, widget= forms.FileInput(attrs={'class':'form-control mb-2 border border-primary'}))
    first_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'First name'}))
    middle_name = forms.CharField(label='',required=False, widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Middle name'}))
    last_name = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Last name'}))
    
    class Meta:
        model = CustomUser
        fields = ['image','first_name', 'middle_name', 'last_name']


# A form for login in of users
class UserLoginForm(forms.ModelForm):
    username = forms.CharField(label='', widget= forms.TextInput(attrs={'class': 'form-control mb-2 border border-primary', 'placeholder':'Username'}))
    password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'class': 'form-control border border-primary', 'placeholder':'Password'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='',required=False, widget=forms.EmailInput(attrs={'class':'form-control mb-2 border border-primary', 'placeholder':'Email'}))
    class Meta:
        model=CustomUser
        fields=['email']