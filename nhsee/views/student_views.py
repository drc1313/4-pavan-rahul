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
import unittest

def studentlisting(request):
    if 'createstudents' in request.POST:
       file_path = request.POST.get('filepath')
       #print(file_path)
       studentssdata=xlrd.open_workbook(file_path)
       sheet = studentssdata.sheet_by_index(0)
       studentnames=sheet.cell_value(0,0)

       for studentnum in range(1,sheet.nrows):
            individualstudent=sheet.row_values(studentnum)
            #print(individualstudent)
            proid=get_object_or_404(project, project_id=individualstudent[4])
            insertstudent=student(id=individualstudent[0],project_id=proid,firstname=individualstudent[1],lastname=individualstudent[2],school=individualstudent[3])
            insertstudent.save()
    if 'deletestudents' in request.POST:
        deleterequest=request.GET.get('delete')
        #if deleterequest=="deletestudents":
        student.objects.all().delete()
    count = 0
    studentl = student.objects.all()
    studentslist=[]
    for students in studentl:
        studentslist.append({"first_name":students.firstname,"last_name":students.lastname,"project_id":students.project_id_id,"school":students.school,"student_id":students.id})
        count = count + 1
    print(count)

    #print(studentslist)
    paginator_projects = Paginator(studentslist, 10)
    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)
    #print(contacts)

    if(count == 96):
        print('all the students are listed')
    else:
        print("some of the data is missing")

    return render(request,'students_template/liststudents.html',{"studentjson":contacts})
