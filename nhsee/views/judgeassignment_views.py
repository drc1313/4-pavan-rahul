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


def judge_listing_assignment(request):



    if 'createjudgeassignment' in request.POST:
       file_path = request.POST.get('filepath')
       judgesdata=xlrd.open_workbook(file_path)
       sheet = judgesdata.sheet_by_index(0)
       judgenames=sheet.cell_value(0,0)

       for judgenum in range(1,sheet.nrows):
            individualjudge=sheet.row_values(judgenum)
            proid=get_object_or_404(project, project_id=individualjudge[0])
            judgeid=get_object_or_404(judge, judge_id=individualjudge[0])
            projectinsert = judgeassignment(project_id=proid,judge_id=judgeid,goal_score=individualjudge[2],plan_score=individualjudge[3],action_score=individualjudge[4],result_analysis_score=individualjudge[5],communication_score=individualjudge[6],raw_score=individualjudge[7])
            projectinsert.save()


    userl = judgeassignment.objects.all()
    projectlist=[]

    for users in userl:

        projectid=users.project_id_id
        judgeid=users.judge_id_id
        goalscore=users.goal_score
        planscore=users.plan_score
        actionscore=users.action_score
        resultanalysisscore=users.result_analysis_score
        communicationscore=users.communication_score
        rawscore=users.raw_score
        projectlist.append({"project_id":projectid,"judge_id":judgeid,"goal_score":goalscore,"plan_score":planscore,"action_score":actionscore,"result_analysis_score":resultanalysisscore,"communication_score":communicationscore,"raw_score":rawscore})
    paginator_projects = Paginator(projectlist, 10)
    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)
    return render(request,'studentassign_template/projectslisting.html',{"projectjson":contacts})
