from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from ..models.judge_model import judge
from ..models.project_model import project
from ..models.judgeassignment_model import judgeassignment
from ..models.student_model import student
from nhsee import models
import uuid
from uuid import UUID
import os
import xlrd
from django.core.paginator import Paginator

def studentlisting(request):


    if 'createstudents' in request.POST:
       print("innnnnnnn")
       file_path = request.POST.get('filepath')
       print(file_path)
       judgesdata=xlrd.open_workbook(file_path)
       sheet = judgesdata.sheet_by_index(0)
       judgenames=sheet.cell_value(0,0)


       for judgenum in range(1,sheet.nrows):
            individualjudge=sheet.row_values(judgenum)
            print(individualjudge)
            proid=get_object_or_404(project, project_id=individualjudge[5])
            student.objects.create(id=individualjudge[1],project_id=proid,firstname=individualjudge[2],lastname=individualjudge[3],school=individualjudge[4])
    judgel = student.objects.all()
    studentslist=[]
    for judges in judgel:

        studentslist.append({"first_name":judges.firstname,"last_name":judges.lastname,"project_id":judges.project_id,"school":judges.school})

    paginator_projects = Paginator(studentslist, 10)
    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)



    return render(request,'students_template/liststudents.html',{"projectjson":contacts})
