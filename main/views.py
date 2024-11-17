from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import StudentForm, ProgramForm, CreditForm
from .models import Program, Student, Credit
from accounts.models import CustomUser

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def dashboardView(request):
    programs = []
    print(programs)

    # if request.user.is_superuser:
    #     programs = Program.objects.all()
    # else:
    #     pass
    #     #programs = Program.objects.filter(id=request.user.profile.program.id)

    context = {
        'programs': programs,
    }
    return render(request, 'main/dashboard.html', context)


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
        return render(request, 'main/addprogram.html', context)


def addCreditView(request, id=None):
    form = CreditForm(initial={'student':id, 'edited_by': request.user.id})
    student = Student.objects.get(id=id)
    context = {
        'form': form,
        'formTitle': (f'Payment for {student.first_name} {student.last_name}')
    }
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            class_name = form.cleaned_data.get('class_name') # Get the username that is submitted
            messages.success(request, f'{class_name} program is created.') # Show sucess message when program is created
            return redirect('dashboard')
    else:
        return render(request, 'main/addprogram.html', context)

