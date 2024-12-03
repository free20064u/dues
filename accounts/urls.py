"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import MyPasswordResetForm, MyPassWordChangeForm
from . import views

urlpatterns = [
   path('login/', views.loginView, name='login'),
   path('logout/', views.logoutView, name='logout'),
   path('register/', views.registerView, name='register'),
   path('edit_profile/<int:id>/', views.editProfileView, name='editProfile'),
   path('all_users/', views.allUsersView, name='allUsers'),
   path('user_details/<int:id>/', views.userDetailView, name='userDetails'),
   path('edit_user/<int:id>/', views.editUserView, name='editUser'),
   path('password-reset/',
         auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            form_class=MyPasswordResetForm,
         ),
         name='password_reset'),
   path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
   path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
   path('password-change/',
         auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            form_class=MyPassWordChangeForm
         ),
         name='password_change'),
   path('password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'
        ),
        name='password_change_done')
]
