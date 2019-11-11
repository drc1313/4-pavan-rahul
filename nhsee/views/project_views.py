from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from ..models.project_model import project
from ..models.judgeassignment_model import judgeassignment
from ..models.judge_model import judge
from nhsee import models
import uuid
from uuid import UUID
import os
import xlrd


def projectslisting(request):
    if "login" in request.POST:
        email=request.GET.get("email")
        password=request.GET.get("password")
    userl = project.objects.all()
    projectlist=[]

    for users in userl:

        project_id=users.project_id
        description=users.description
        project_title=users.project_title
        project_category=users.project_category
        projectidlist=judgeassignment.objects.filter(project_id=project_id)
        projectcount=[]

        for individualpoject in projectidlist:
            projectcount.append(individualpoject)

        if len(projectcount) <= 5:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description})

        else:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description,"projectfilled":True})
    paginator_projects = Paginator(projectlist, 10) # Show 25 contacts per page
    print(paginator_projects)

    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)

    if 'createprojects' in request.POST:
       file_path = request.POST.get('filepath')
       projectsdata=xlrd.open_workbook(file_path)
       sheet = judgesdata.sheet_by_index(0)
       projectnames=sheet.cell_value(0,0)

       for projectnum in range(1,sheet.nrows):
            individualproject=sheet.row_values(projectnum)
            projectinsert = project(project_id=individualproject[2],project_title=individualproject[1],project_category=individualproject[0],description=individualproject[3])
            projectinsert.save()
    if 'projectjudges' in request.POST:
            projectid = request.POST.get('project_id')
            judgesq = judgeassignment.objects.filter(project_id=projectid)



            judge_list=[]
            for judges in judgesq:
                judgestatus=judge.objects.filter(judge_id=judges.judge_id)
                judge_list.append({"judge_name":str(judgestatus.fname)+" "+str(judgestatus.lname),"judge_id":judges.judge_id,"project_id":project_id,"judgestatus":True})

            return render(request,'projects_template/assignjudge.html',{"judgesjson":judge_list})


    return render(request,'swapprojectassigning.html',{"projectjson":contacts})
