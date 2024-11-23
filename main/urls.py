
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('contact/', views.contactView, name='contact'),
    path('program/', views.programView, name='program'),
    path('add_program/', views.addProgramView, name='addProgram'),
    path('edit_program/<int:id>/', views.editProgramView, name='editProgram'),
    path('add_student/', views.addStudentView, name='addStudent'),
    path('student/<int:id>/', views.studentView, name='student'),
    path('editStudent/<int:id>/', views.editStudentView, name='editStudent'),
    path('add_credit/<int:id>/', views.addCreditView, name='addCredit'),
    path('student_list/<int:id>/', views.studentListView, name='studentList'),
    path('messages/', views.messageView, name='message'),
    path('read_message/<int:id>/', views.readMessageView, name='read_message'),
    path('update/', views.webhook, name='update'),  
]
