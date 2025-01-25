import os
from decimal import Decimal
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm, ProgramForm, CreditForm, MessageForm, TeacherCreditForm
from .models import Program, Student, Credit, Message, TeacherCredit
from accounts.models import CustomUser
from extraction.forms import FileForm

from .context_processors import getProgramTotalCredit

from git import Repo

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


@login_required
def dashboardView(request):
    # Getting information about programs assigned to users
    if request.user.is_superuser:
        programs = Program.objects.all()
        for program in programs:
            program.getProgramTotalCredit = getProgramTotalCredit(program.id)
    else:
        programs = request.user.program.all()
        for program in programs:
            program.getProgramTotalCredit = getProgramTotalCredit(program.id)

    

    # Total payment recieved by a user
    totalCredit=0
    credits = Credit.objects.filter(edited_by=request.user.id)
    for credit in credits:
        totalCredit = totalCredit + credit.amount


    context = {
        'programs': programs,
        'totalCredit': totalCredit,
        'fileForm': FileForm(),
        'teacherTotalCredit': TeacherCredit.totalCredit(TeacherCredit),
        'teacherCrditBalance': totalCredit - TeacherCredit.totalCredit(TeacherCredit)
    }
    return render(request, 'main/dashboard.html', context)


@login_required
def contactView(request):
    form = MessageForm()
    map_url=os.getenv('map_url')
    context = {
        'form': form,
        'formTitle':'Contact Us',
        'map_url':map_url,
    }
    # Sending message to the admin
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
            return render(request, 'main/contact.html', context)     
    else:
        return render(request, 'main/contact.html', context)


@login_required
def programView(request):
    programs = Program.objects.all()
    context = {
        'programs': programs,
    }
    return render(request, 'main/program.html', context )


@login_required
def addProgramView(request):
    form = ProgramForm()
    context = {
        'formTitle': 'Add Program',
        'form': form,
    }
    # Adding program to the database
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            program = form.cleaned_data.get('program_name') # Get the program that is submitted
            messages.success(request, f'{program} program is created.') # Show sucess message when program is created
            if request.POST['condition'] == 'on':
                return redirect('dashboard')
            else:
                return redirect('/add_program/')
    else:
        return render(request, 'main/addProgram.html', context)

@login_required
def editProgramView(request, id=None):
    form = ProgramForm(instance=Program.objects.get(id=id))
    context ={
        'form': form,
        'formTitle':'Edit Program',
    }
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=Program.objects.get(id=id))
        if request.POST['condition'] == 'on':
            if form.is_valid():
                form.save()
                messages.success(request, 'Program updated successfully')
                return redirect('/program/')
        else:
            program = Program.objects.get(id=id)
            for student in Student.objects.all():
                print(student.program, program)
                if student.program == program:
                    messages.error(request, 'You cant delete a program assigned to students')
                    return redirect('/program/')
                

            program.delete()
            messages.success(request, 'Program deleted successfully')
            return redirect('/program/')
            
    else:
        return render(request, 'main/addProgram.html', context)


@login_required
def studentListView(request, id=None):
    # Showing the list about the students that offere a certain program
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
        return render(request, 'main/studentList.html', context)
    else:
        return render(request, 'main/studentList.html', context)


@login_required
def studentView(request, id=None):
    # Showing a detail view about a student
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


@login_required
def addStudentView(request):
    # Adding a student information to the database
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
            messages.success(request, f'Student {first_name} {middle_name} {last_name} is created.') # Show sucess message when program is created
            if request.POST['condition'] == 'on':
                return redirect('dashboard')
            else:
                return redirect('/add_student/')
    else:
        return render(request, 'main/addProgram.html', context)


@login_required
def editStudentView(request, id=None):
    # Editing information about student
    user_obj = Student.objects.get(id=id)
    form = StudentForm(instance=user_obj)

    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=Student.objects.get(id=id))
        if form.is_valid():
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
def addCreditView(request, id=None):
    # Making payment on behalf of student
    form = CreditForm(initial={'student':id, 'edited_by': request.user.id})
    student = Student.objects.get(id=id)
    context = {
        'form': form,
        'formTitle': (f'Payment for {student.first_name} {student.last_name}')
    }
    if request.method == 'POST':
        if Decimal(request.POST['amount']) >= Decimal(0) and Decimal(request.POST['amount']):
            form = CreditForm(request.POST)
            if form.is_valid():
                form.save()
                class_name = form.cleaned_data.get('amount') # Get the username that is submitted
                messages.success(request, f'GHc {class_name} is paid for {student}.') # Show sucess message when program is created
                return redirect('dashboard')
        else:
            messages.error(request, 'Negative values are not allowed.')
            return render(request, 'main/addProgram.html', context)
    else:
        return render(request, 'main/addProgram.html', context)


@login_required
def messageView(request):
    # Sending message to the database
    contact_messages = Message.objects.all().order_by('-id')
    
    context = {
        'contact_messages': contact_messages,
    }
    return render(request, 'main/message.html', context)


@login_required
def readMessageView(request, id=None):
    # Reading the messages
    message = Message.objects.get(id=id)
    message.is_read = True
    message.save()
    context = {
        'message': message,
    }
    return render(request, 'main/readMessage.html', context)

# Updating information on hosting server when changes are pushed to github repo.
@csrf_exempt
def webhook(request):
    repo = Repo('/home/wbmzionscience/dues')
    repo.remotes.origin.pull()
    return HttpResponse('pulled_success')


@login_required
def teacherCreditView(request, id=None):
    form = TeacherCreditForm(initial={'teacher':id, 'edited_by': request.user.id})
    teacher = CustomUser.objects.get(id=id)
    context = {
        'form': form,
        'formTitle': 'Pay To Admin'
    }
    if request.method == 'POST':
        form = TeacherCreditForm(request.POST)
        if Decimal(request.POST['amount']) >= Decimal(0):
            if form.is_valid():
                form.save()
                messages.success(request, f'{teacher} is credited')
                return redirect(f'/accounts/user_details/{id}')
            else:
                return render(request, 'main/pay_to_admin.html', context)
        else:
            messages.error(request, 'Negative values are not accepted')
            return render(request, 'main/pay_to_admin.html', context)
    else:
        return render(request, 'main/pay_to_admin.html', context)
    

def paymentLogView(request, id=None):
    payment_logs = TeacherCredit.objects.filter(teacher_id=id)
    teacher = CustomUser.objects.get(id=id)

    paid_to_admin = 0
    teacherCredits = TeacherCredit.objects.filter(teacher_id=id)
    for teacherCredit in teacherCredits:
        paid_to_admin += teacherCredit.amount
    
    totalCredit=0
    credits = Credit.objects.filter(edited_by=id)
    for credit in credits:
        totalCredit = totalCredit + credit.amount

    context = {
        'payment_logs': payment_logs,
        'teacher': teacher,
        'paid_to_admin': paid_to_admin,
        'totalCredit': totalCredit,
        'balance': totalCredit-paid_to_admin,
    }
    return render(request, 'main/teacher.html', context)