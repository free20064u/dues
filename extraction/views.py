from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

from main.models import Student

import openpyxl

@login_required
def import_data_to_db(request):
    if request.method == 'POST':
        file = request.FILES['file']
        program=request.POST['program']

        wb = openpyxl.load_workbook(file)
        lineCount=0
        lines=[]
        for worksheet in wb:
            for row in worksheet.iter_rows():
                names = str(row[0].value).split(' ')
                if len(names) == 1:
                    lineCount += 1
                    lines.append(lineCount)
                elif len(names) == 2:
                    Student.objects.create(program_id=program, first_name=names[1],middle_name=None, last_name=names[0])
                elif len(names) == 3:
                    Student.objects.create(program_id=program, first_name=names[1],middle_name=names[2], last_name=names[0])
                else:
                    Student.objects.create(program_id=program, first_name=names[1],middle_name=f'{names[2]}  {names[3]}', last_name=names[0])
        if lineCount > 0:
            messages.error(request, f'Following lines {lines} where not added')
        return redirect('dashboard')