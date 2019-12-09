from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from ..models.judge_model import judge
from ..models.project_model import project
from ..models.judgeassignment_model import judgeassignment
from django.core.paginator import Paginator
from nhsee import models
import uuid
from uuid import UUID
import os
import xlrd

def judgeslisting(request):

    if 'createjudges' in request.POST:
       file_path = request.POST.get('filepath')
       #print(file_path,"ggggggggggggggg")
       judgesdata=xlrd.open_workbook(file_path)
       sheet = judgesdata.sheet_by_index(0)
       judgenames=sheet.cell_value(0,0)

       for judgenum in range(1,sheet.nrows):
            individualjudge=sheet.row_values(judgenum)
            projectinsert = judge(judge_id=individualjudge[0],fname=individualjudge[1],lname=individualjudge[2])
            projectinsert.save()
    if 'deletejudges' in request.POST:
      deleterequest=request.GET.get('delete')
      #if deleterequest=="deletestudents":
      judge.objects.all().delete()


    if 'judgeprojects' in request.POST:
                judgeid=request.POST.get('judge_id')
                #print(judgeid,"kkkkkkkkkk-----")
                judgeprojects=judgeassignment.objects.filter(judge_id_id=judgeid)
                judge_list=[]

                for judges in judgeprojects:
                    print(judges.judge_id_id)
                    projectid=judges.project_id_id
                    judgenames=project.objects.filter(project_id=projectid)

                    for judgesinfo in judgenames:
                        judge_list.append({"project_name":str(judgesinfo.project_title),"project_description":str(judgesinfo.description),"judge_id":judgeid,"project_id":projectid})
                return render(request,'judges_templates/assignjudgelist.html',{"judgesjson":judge_list})


    judgel = judge.objects.all()
    judge_list=[]

    for judges in judgel:
        judgestatus=judgeassignment.objects.filter(judge_id=judges.judge_id)
        assign_judge_list=[]

        for judge_ids in judgestatus:
            assign_judge_list.append(judge_ids.judge_id_id)

        judgestatus=len(assign_judge_list)
        if judgestatus > 5:
                judge_list.append({"judge_name":str(judges.fname)+" "+str(judges.lname),"judge_id":judges.judge_id,"judgestatus":True})
        else:
               judge_list.append({"judge_name":str(judges.fname)+" "+str(judges.lname),"judge_id":judges.judge_id})
    paginator_projects = Paginator(judge_list, 10)
    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)



    return render(request,'judges_templates/listjudges.html',{"judgesjson":contacts})
