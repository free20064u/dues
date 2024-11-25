from django.shortcuts import render
from .models import *
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
from main.models import Student

import openpyxl


def export_data_to_excel(request):
    # Retrieve all Employee objects from the database
    objs = Student.objects.all()
    data = []
    for obj in objs:
        data.append({
            "first_name": obj.first_name,
            "middle_name": obj.middle_name,
            "last_name": obj.last_name,
            'program':obj.program,
            'image':obj.image,
        })
    pd.DataFrame(data).to_excel('output.xlsx')
    return JsonResponse({
        'status': 200
    })


def import_data_to_db(request):
    data_to_display = None
    if request.method == 'POST':
        file = request.FILES['file']
        program=request.POST['program']


        wb = openpyxl.load_workbook(file)
        for worksheet in wb:
            print(worksheet)
            for row in worksheet.iter_rows():
                names = str(row[0].value).split(' ')
                if len(names) == 1:
                    #messages.error(request, '')
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
                
        # obj = File.objects.create(
        #     file=file
        # )
        # path = file.file
        # df = pd.read_excel(path, index_col=0)
        # data_to_display = df.to_csv()

    return render(request, 'extraction/excel.html',)