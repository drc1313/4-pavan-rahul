from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from ..models.judge_model import judge
from ..models.project_model import project
from ..models.judgeassignment_model import judgeassignment
from nhsee import models
import uuid
from uuid import UUID
import os
import xlrd

def judgeslisting(request):
    print("in judgelist")
    judgel = judge.objects.all()
    #projects=open("/home/arvind/Downloads/test.xlsm","r")
    #data =projects.encode('utf-8').strip()
    #data=projects.read()
    judge_list=[]
    for judges in judgel:
        print(judges.judge_id)
        #print(users.project_id)
        judgestatus=judgeassignment.objects.filter(judge_id=judges.judge_id)

        judgelist=[]
        for judgeids in judgestatus:

            judgelist.append(judgeids.judge_id)

        judgestatus=len(judgelist)

        if judgestatus > 5:
                judge_list.append({"judge_name":str(judges.fname)+" "+str(judges.lname),"judge_id":judges.judge_id,"judgestatus":True})
        else:
               judge_list.append({"judge_name":str(judges.fname)+" "+str(judges.lname),"judge_id":judges.judge_id})






    if 'createjudges' in request.POST:
       print("innnnnnnnnnnnnnnnnnnnnnnnnn")
            # create a form instance and populate it with data from the request:
       file_path = request.POST.get('filepath')
       print(file_path)
       judgesdata=xlrd.open_workbook(file_path)
       sheet = judgesdata.sheet_by_index(0)
       judgenames=sheet.cell_value(0,0)


    #print(judgescount)

       for judgenum in range(1,sheet.nrows):
            individualjudge=sheet.row_values(judgenum)
            projectinsert = judge(judge_id=individualjudge[0],fname=individualjudge[1],lname=individualjudge[2])
            projectinsert.save()
            print(individualjudge)


    if 'judgeprojects' in request.POST:
                judgeid=request.POST.get('judge_id')
                print(judgeid)
                judgeprojects=judgeassignment.objects.filter(judge_id_id=judgeid)
                #company = get_object_or_404(judgeassignment, judge_id=judgeid)

                judge_list=[]
                for judges in judgeprojects:
                    print(judges.judge_id_id)
                    projectid=judges.project_id_id

                    judgenames=project.objects.filter(project_id=projectid)
                    for judgesinfo in judgenames:


                        judge_list.append({"project_name":str(judgesinfo.project_title),"project_description":str(judgesinfo.description),"judge_id":judgeid,"project_id":projectid})
                return render(request,'assignjudgelist.html',{"judgesjson":judge_list})
    return render(request,'judges_templates/listjudges.html',{"judgesjson":judge_list})
