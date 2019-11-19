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
    userl = project.objects.all()
    projectlist=[]

    for users in userl:

        project_id=users.project_id
        description=users.description
        project_title=users.project_title
        project_category=users.project_category
        projectidlist=judgeassignment.objects.filter(project_id_id=project_id)
        projectcount=[]
        totalscores_list=[]
        average_scorelist=[]
        for individualpoject in projectidlist:
            projectcount.append(individualpoject)
            projectid=individualpoject.project_id_id
            judgeid=individualpoject.judge_id_id
            goalscore=individualpoject.goal_score
            planscore=individualpoject.plan_score
            actionscore=individualpoject.action_score
            resultanalysisscore=individualpoject.result_analysis_score
            communicationscore=individualpoject.communication_score
            rawscore=individualpoject.raw_score
            if goalscore or planscore or actionscore or resultanalysisscore or communicationscore  == None:
                totalscore=0
            else:
                totalscore=goalscore+planscore+actionscore+resultanalysisscore+communicationscore
            average_scorelist.append(totalscore/5)
            totalscores_list.append(totalscore)
        project_avg_score=sum(average_scorelist)    
        project_score=sum(totalscores_list)
        print(project_score)    
        
        n=1


        if len(projectcount) <= 5:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description,"total_score":project_score,"average_score":project_avg_score})

        else:
            projectlist.append({"project_id":project_id,"project_title":project_title,"project_category":project_category,"description":description,"projectfilled":True,"total_score":project_score,"average_score":project_avg_score})
    projectranking=sorted(projectlist, key = lambda i: i['total_score'])
    print(projectranking)
    #originalranking=projectranking.reverse()
    originalranking = [ele for ele in reversed(projectranking)]
    print(originalranking)
    for assignrank in originalranking:
            assignrank["rank"]=n
            n=n+1
    paginator_projects = Paginator(originalranking, 10) 
    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)
        

    return render(request,'projects_template/listprojects.html',{"projectjson":contacts})
