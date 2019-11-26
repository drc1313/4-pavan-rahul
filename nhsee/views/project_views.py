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
from django.db import IntegrityError


def projectslisting(request):



    if 'createprojects' in request.POST:
       file_path = request.POST.get('filepath')
       judgesdata=xlrd.open_workbook(file_path)
       sheet = judgesdata.sheet_by_index(0)
       judgenames=sheet.cell_value(0,0)

       for judgenum in range(1,sheet.nrows):
            individualjudge=sheet.row_values(judgenum)
            projectinsert = project(project_id=individualjudge[2],project_title=individualjudge[1],project_category=individualjudge[0],description=individualjudge[3])
            projectinsert.save()
    if 'projectjudges' in request.POST:
            projectid = request.POST.get('project_id')
            judgesq = judgeassignment.objects.filter(project_id=projectid)



            judge_list=[]
            for judges in judgesq:
                judgestatus=judge.objects.filter(judge_id=judges.judge_id)
                for judgedetails in judgestatus:
                    judge_list.append({"judge_name":str(judgedetails.fname)+" "+str(judgedetails.lname),"judge_id":judges.judge_id,"project_id":project_id,"judgestatus":True})

            return render(request,'projects_template/assignjudge.html',{"judgesjson":judge_list})

    if 'deleteprojects' in request.GET:
            deleterequest=request.GET.get('delete')
            if deleterequest=="deleteprojects":
                try:
                    project.objects.all().delete()

                except IntegrityError as e:
                    pass
    userl = project.objects.all()
    projectlist=[]

    for users in userl:

        project_id=users.project_id
        description=users.description
        project_title=users.project_title
        project_category=users.project_category
        projectidlist=judgeassignment.objects.filter(project_id_id=project_id)
        projectcount=[]
        average_scorelist=[]
        for individualpoject in projectidlist:
            projectcount.append(individualpoject)
            projectid=individualpoject.project_id_id
            judgeid=individualpoject.judge_id_id
            rawscore=individualpoject.raw_score
            average_scorelist.append(rawscore)
        project_score=sum(average_scorelist)
        if len(average_scorelist) == 0:
            project_avg_score=0
        else:
            project_avg_score=project_score/len(average_scorelist)






        if len(projectcount) <= 5:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description,"total_score":project_score,"average_score":project_avg_score})

        else:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description,"projectfilled":True,"total_score":project_score,"average_score":project_avg_score})
    projectranking=sorted(projectlist, key = lambda i: i['average_score'])
    originalranking = [ele for ele in reversed(projectranking)]
    n=1
    for assignrank in originalranking:
            assignrank["rank"]=n
            n=n+1
    paginator_projects = Paginator(originalranking, 10)
    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)


    return render(request,'projects_template/listprojects.html',{"projectjson":contacts})
