from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import project,judge,judge_assignment
from nhsee import models
import uuid
from uuid import UUID
import os
import xlrd
# Create your views here.

def projectslisting(request):
    userl = project.objects.all()
    #projects=open("/home/arvind/Downloads/test.xlsm","r")
    #data =projects.encode('utf-8').strip()
    #data=projects.read()
    projectlist=[]
    for users in userl:
        #print(users.project_id)
        project_id=users.project_id
        description=users.description
        project_title=users.project_title
        project_category=users.project_category
        projectidlist=judge_assignment.objects.filter(project_id=project_id)
        projectcount=[]

        for individualpoject in projectidlist:
            projectcount.append(individualpoject)
        if len(projectcount) <= 5:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description})
        else:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description,"projectfilled":True})







    if 'createprojects' in request.POST:
            # create a form instance and populate it with data from the request:
       file_path = request.POST.get('filepath')
       judgesdata=xlrd.open_workbook(file_path)
       sheet = judgesdata.sheet_by_index(0)
       judgenames=sheet.cell_value(0,0)


    #print(judgescount)

       for judgenum in range(1,sheet.nrows):
            individualjudge=sheet.row_values(judgenum)
            projectinsert = project(project_id=individualjudge[2],project_title=individualjudge[1],project_category=individualjudge[0],description=individualjudge[3])
            projectinsert.save()

    if 'assignproject' in request.POST:

            projectid = request.POST.get('project_id')
            judgesq = judge.objects.all()


            judge_list=[]
            for judges in judgesq:
                judgestatus=judge_assignment.objects.filter(project_id=projectid)
                judgelist=[]
                for judgeids in judgestatus:
                    judgelist.append(judgeids)
                print(judgelist)
                judgestatus=len(judgelist)
                if judgestatus <= 5:
                    judge_list.append({"judge_name":str(judges.fname)+" "+str(judges.lname),"judge_id":judges.judge_id,"project_id":project_id,"judgestatus":True})
                else:
                    judge_list.append({"judge_name":str(judges.fname)+" "+str(judges.lname),"judge_id":judges.judge_id,"project_id":project_id})
            return render(request,'assignjudge.html',{"judgesjson":judge_list})
    if 'assignjudge' in request.POST:
                projectid=request.POST.get('project_id')
                judgeid=request.POST.get('judge_id')


                print(projectid)
                print(judgeid)
                judge_new = get_object_or_404(judge, judge_id=judgeid)

                project_new = get_object_or_404(project, project_id=projectid)
                judge_assignment.objects.create(judge_id=judge_new,project_id=project_new)
                print("created")






    return render(request,'projectslisting.html',{"projectval":projectlist})
