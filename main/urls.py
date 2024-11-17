
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('add_program/', views.addProgramView, name='addProgram'),
    path('add_student/', views.addStudentView, name='addStudent'),
    path('student/<int:id>/', views.studentView, name='student'),
    path('editStudent/<int:id>/', views.editStudentView, name='editStudent'),
    path('add_credit/<int:id>/', views.addCreditView, name='addCredit'),
    path('program/<int:id>/', views.programView, name='program'),  
]
