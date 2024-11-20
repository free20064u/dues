from decimal import Decimal
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm, ProgramForm, CreditForm, MessageForm
from .models import Program, Student, Credit
from accounts.models import CustomUser

from git import Repo

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def dashboardView(request):
    programs = []

    if request.user.is_superuser:
        programs = Program.objects.all()
    else:
        programs = request.user.program.all()

    totalCredit=0
    credits = Credit.objects.filter(edited_by=request.user.id)
    for credit in credits:
        totalCredit = totalCredit + credit.amount

    context = {
        'programs': programs,
        'totalCredit': totalCredit,
    }
    return render(request, 'main/dashboard.html', context)

def contactView(request):
    form = MessageForm()
    context = {
        'form': form,
        'formTitle':'Contact Us',
    }
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Message is sent')
            return redirect('dashboard')
        else:
            context['form'] = form
            return render(request, 'main/addProgram.html', context)     
    else:
        return render(request, 'main/addProgram.html', context)


def addProgramView(request):
    form = ProgramForm()
    context = {
        'formTitle': 'Add Program',
        'form': form,
    }
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            program = form.cleaned_data.get('program_name') # Get the username that is submitted
            messages.success(request, f'{program} program is created.') # Show sucess message when program is created
            return redirect('dashboard')
    else:
        return render(request, 'main/addProgram.html', context)


def programView(request, id=None):
    stuObj=[]
    
    students = Student.objects.filter(program=id)

    for student in students:
        obj = {}
        obj['student'] = Student.objects.get(id=student.id)
        obj['studentTotalCredit']= Student.objects.get(id=student.id).getStudentTotalCredit(id=student.id)
        obj['studentBalance']= Student.objects.get(id=student.id).getStudentBalance(id=student.id)

        stuObj.append(obj)
    context = {
        'stuObj': stuObj,
    }
    if request.method == 'POST':
        stuObj=[]
        students = Student.objects.filter(first_name__contains=request.POST['name'], program=id)
        for student in students:
            obj = {}
            obj['student'] = Student.objects.get(id=student.id)
            obj['studentTotalCredit']= Student.objects.get(id=student.id).getStudentTotalCredit(id=student.id)
            obj['studentBalance']= Student.objects.get(id=student.id).getStudentBalance(id=student.id)

            stuObj.append(obj)
        context['stuObj']=stuObj
        return render(request, 'main/program.html', context)
    else:
        return render(request, 'main/program.html', context)


def studentView(request, id=None):
    context = {
        'student': Student.objects.get(id=id),
        'payments': Credit.objects.filter(student_id=id),
        'studentTotalCredit': Student.objects.get(id=id).getStudentTotalCredit(id=id),
        'studentBalance': Student.objects.get(id=id).getStudentBalance(id=id),
    }
    if request.method == 'POST':
        pass
    else:
        return render(request, 'main/student.html', context)

def addStudentView(request):
    form = StudentForm()
    context = {
        'form': form,
        'formTitle':'Add Student'
    }
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name') # Get the username that is submitted
            middle_name = form.cleaned_data.get('middle_name') # Get the username that is submitted
            last_name = form.cleaned_data.get('last_name') # Get the username that is submitted
            messages.success(request, f'{first_name} {middle_name} {last_name} program is created.') # Show sucess message when program is created
            return redirect('dashboard')
    else:
        return render(request, 'main/addProgram.html', context)

def editStudentView(request, id=None):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student {student} details updated')
            return redirect('dashboard')
    else:
        return render(request, 'main/addProgram.html', context)

def addCreditView(request, id=None):
    form = CreditForm(initial={'student':id, 'edited_by': request.user.id})
    student = Student.objects.get(id=id)
    context = {
        'form': form,
        'formTitle': (f'Payment for {student.first_name} {student.last_name}')
    }
    if request.method == 'POST':
        if Decimal(request.POST['amount']) >= Decimal(0) and Decimal(request.POST['amount']) <= Decimal(student.getStudentBalance(id=id)):
            form = CreditForm(request.POST)
            if form.is_valid():
                form.save()
                class_name = form.cleaned_data.get('amount') # Get the username that is submitted
                messages.success(request, f'GHc {class_name} is paid for {student}.') # Show sucess message when program is created
                return redirect('dashboard')
        else:
            messages.error(request, 'Negative values are not allowed \n Amount cant be more that what the student owe.')
            return render(request, 'main/addProgram.html', context)
    else:
        return render(request, 'main/addProgram.html', context)


@csrf_exempt
def webhook(request):
    repo = Repo('/home/wbmzionscience/dues')
    repo.remotes.origin.pull()
    return HttpResponse('pulled_success')