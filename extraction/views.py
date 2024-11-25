from django.shortcuts import render
from django.contrib import messages
from .models import *
import pandas as pd

from main.models import Student

import openpyxl


def import_data_to_db(request):
    if request.method == 'POST':
        file = request.FILES['file']
        program=request.POST['program']

        wb = openpyxl.load_workbook(file)
        for worksheet in wb:
            print(worksheet)
            for row in worksheet.iter_rows():
                names = str(row[0].value).split(' ')
                if len(names) == 1:
                    messages.error(request, '')
                    pass
                elif len(names) == 2:
                    print(f'first_name: {names[0]} last_name: {names[1]}')
                    Student.objects.create(program_id=program, first_name=names[1], last_name=names[0])
                elif len(names) == 3:
                    print(f'first_name: {names[0]} middle_name: {names[1]} last_name: {names[2]}')
                    Student.objects.create(program_id=program, first_name=names[1],middle_name=names[2], last_name=names[0])

                else:
                    print(f'first_name: {names[0]} middle_name: {names[1]} last_name: {names[2]} {names[3]}')
                    Student.objects.create(program_id=program, first_name=names[1],middle_name=(names[2] ,names[3]), last_name=names[0])

    return render(request, 'extraction/excel.html',)