import os
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import CustomUser

from .forms import UserLoginForm, UserRegisterForm, ProfileUpdateForm, AdminUserUpdateForm, PasswordResetForm

from main.models import Credit, Program

# Create your views here.
def registerView(request):
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('login') # Redirect user to Homepage
        else:
            return HttpResponse('form not valid')
    else:
        return render(request, 'accounts/register.html', context)


def logoutView(request):
    logout(request)
    return redirect('index')


def loginView(request):
    form = UserLoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user != None:
            login(request, user)
            messages.success(request, 'You have logged in successfully')
            return redirect('dashboard')
        else:
            context['form'] = UserLoginForm(request.POST)
            messages.error(request, 'Username or password incorrect')
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', context)
    

@login_required
def editProfileView(request, id=None):
    user_obj=CustomUser.objects.get(id=id)
    form = ProfileUpdateForm(instance=user_obj)
    context = {
        'form': form,
        'formTitle': 'Update Profile',
    }
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if user_obj.imageURL() != '/media/profile/wbm-logo.png':
                try:
                    os.remove(user_obj.image.path)
                    if request.FILES['image']=='':
                        obj = form.save(commit=False)
                        obj.image='profile/wbm-logo.png'
                        obj.save()
                        messages.success(request, 'Profile updated successfully')
                        return redirect('dashboard')
                    else:
                        form.save()
                        messages.success(request, 'Profile updated successfully')
                        return redirect('dashboard')
                except:
                    obj = form.save(commit=False)
                    obj.image='profile/wbm-logo.png'
                    obj.save()
                    messages.success(request, 'Profile updated successfully')
                    return redirect('dashboard')
            else:
                if request.FILES['image']=='':
                    obj = form.save(commit=False)
                    obj.image='profile/wbm-logo.png'
                    obj.save()
                    messages.success(request, 'Profile updated successfully')
                    return redirect('dashboard')
                else:
                    form.save()
                    messages.success(request, 'Profile updated successfully')
                    return redirect('dashboard')
        else:
            context['form']=form
            messages.success(request, 'Profile updated successfully', context) 
    else:
        return render(request, 'main/addProgram.html', context)
    

@login_required
def allUsersView(request):
    context = {
        'users': CustomUser.objects.all()
    }
    return render(request, 'accounts/users.html', context)


@login_required
def userDetailView(request, id=None):
    user = CustomUser.objects.get(id=id)
    totalCredit=0
    credits = Credit.objects.filter(edited_by=id)
    for credit in credits:
        totalCredit = totalCredit + credit.amount

    context = {
        'user': user,
        'totalCredit': totalCredit,
    }
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/userDetail.html', context)

@login_required
def editUserView(request, id=None):
    form = AdminUserUpdateForm(instance=CustomUser.objects.get(id=id))
    context = {
        'form': form,
        'formTitle': 'Edit Details',
    }
    if request.method == 'POST':
        form = AdminUserUpdateForm(request.POST, instance=CustomUser.objects.get(id=id))
        if form.is_valid():
            form.save()
            messages.success(request, 'User information updated successfully')
            return redirect(f'/accounts/user_details/{id}/')
        else:
            return HttpResponse('Invalid form')
    else:
        return render(request, 'main/addProgram.html', context)
    
def PasswordResetView(request):
    pass

def PasswordResetDoneView(request):
    pass

def PasswordResetConfirmView(request):
    pass

def PasswordResetCompleteView(request):
    pass