from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from ..models.project_model import project
from ..models.judgeassignment_model import judgeassignment
from ..models.judge_model import judge
from ..models.student_model import student
from nhsee import models
import uuid
from uuid import UUID
import os
import xlrd
from django.db import IntegrityError
import statistics

def projectslisting(request):




    if 'projectjudges' in request.POST:
            projectid = request.POST.get('project_id')
            #print(projectid,"sssssssssssssssss")
            judgesq = student.objects.filter(project_id=projectid)

            judge_list=[]
            for judgedetails in judgesq:

                    judge_list.append({"studentid":judgedetails.id,"student_name":str(judgedetails.firstname)+" "+str(judgedetails.lastname),"project_id":projectid,"school":judgedetails.school})

            return render(request,'projects_template/assignjudge.html',{"judgesjson":judge_list})

    if 'deleteprojects' in request.GET:
            deleterequest=request.GET.get('delete')
            #print(deleterequest)
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

        rawscore_judge={}
        rawscore_judgelist=[]
        for individualpoject in projectidlist:
            projectcount.append(individualpoject)
            projectid=individualpoject.project_id_id
            judgeid=individualpoject.judge_id_id
            rawscore=individualpoject.raw_score
            average_scorelist.append(rawscore)


# z score
            projectidlist=judgeassignment.objects.filter(judge_id_id=judgeid)
            forzscore=[]
            rawscore_judge={}
            for alljudgeprojects in projectidlist:

                forzscore.append(alljudgeprojects.raw_score)

            rawscore_judge["raw_score"]=forzscore
            rawscore_judge["rawscore_individual"]=rawscore
            rawscore_judgelist.append(rawscore_judge)
            #print(rawscore_judgelist)
        if  len(average_scorelist)==0:
            average_score=0
        else:
            average_score=sum(average_scorelist)/len(average_scorelist)
        zscoreavg=0

        zscorelist=[]
        for rawscorejudgemapping in rawscore_judgelist:
            project_score=sum(rawscorejudgemapping["raw_score"])
            if len(rawscorejudgemapping["raw_score"]) == 0:
                project_avg_score=0
            else:
                project_avg_score=project_score/len(rawscorejudgemapping["raw_score"])
            z_scoreindividua     = (rawscorejudgemapping["rawscore_individual"] - project_avg_score) / statistics.stdev(rawscorejudgemapping["raw_score"])
            zscorelist.append(z_scoreindividua)

        if len(zscorelist)==0:
           zscoreresult=0
        else:
            zscoreresult=sum(zscorelist)/len(zscorelist)

        if len(projectcount) <= 5:
            projectlist.append({"project_id":project_id,"project_title":project_title,"judge_details":rawscore_judgelist,"project_category":project_category,"description":description,"total_score":project_score,"average_score":average_score,"z_score":zscoreresult})

        else:
            projectlist.append({"project_id":project_id,"project_title":project_title,"judge_details":rawscore_judgelist,"project_category":project_category,"description":description,"projectfilled":True,"total_score":project_score,"average_score":average_score,"z_score":zscoreresult})


# rank based on  average score
    n=1
    projectranking=sorted(projectlist, key = lambda i: i['average_score'])
    originalranking = [ele for ele in reversed(projectranking)]
    for assignrank in originalranking:
            assignrank["rank"]=n
            n=n+1


#scaled score
    k=0
    rawscorelist=[]
    for minimumsc in originalranking:
        rawscorelist.append(minimumsc["average_score"])
    minimumscore=min(i for i in rawscorelist if i > k)

    maximumscore=originalranking[0]["average_score"]
    rangeval=maximumscore-minimumscore
    for scaledscore in originalranking:
        projectavgscore=scaledscore["average_score"]
        scaled = ((projectavgscore - minimumscore)/rangeval)*25 +25
        scaledscore["scaled_score"]=scaled
#scaled rank....
    c=1
    projectrawranking=sorted(projectlist, key = lambda i: i['total_score'])
    originalrawranking = [ele for ele in reversed(projectrawranking)]
    for assignrawrank in originalrawranking:
            assignrawrank["rawscore_rank"]=c
            c=c+1
    for scaledrank in originalrawranking:
        #print(scaledrank)
        judgeprojects=scaledrank["judge_details"]
        avgranklist=[]

        for individualjudge in judgeprojects:
           count_of_judge_projects = len(individualjudge["raw_score"])


           scaledrankno=individualjudge["rawscore_individual"]
           #print(individualjudge["raw_score"],"pppppppppppppppppp")

           rankfun=individualjudge["raw_score"]
           ranksort=sorted(rankfun, key = lambda x:int(x))

           for i in range(0, len(ranksort)):
                ranksort[i] = int(ranksort[i])
           #print(ranksort)
           ranksort.reverse()
           #print(ranksort)
           rank=ranksort.index(individualjudge["rawscore_individual"])+1
           #print(rank)



           avg_rank_project=(count_of_judge_projects-rank)/(count_of_judge_projects-1)
           avgranklist.append(avg_rank_project)



        if len(avgranklist)==0:
            scaledrank["average_rank"]=0
        else:
            averagera=sum(avgranklist)/len(avgranklist)
            scaledrank["average_rank"]=averagera

    scaledranklist=[]
    for minimumavg in originalrawranking:

        scaledranklist.append(minimumavg["average_rank"])

    minimum_avg_score=min(scaledranklist)

    maximum_avg_score = max(scaledranklist)

    rangevalue=maximum_avg_score-minimum_avg_score
    for finalscaledrank in originalrawranking:
        finalscaledrank["scaled_rank"]=(((finalscaledrank["average_rank"]-minimum_avg_score)/rangevalue)*25)+25

#scaled z-score
    zscorescalelist=[]
    for zscorescale in originalrawranking:
        zscorescalelist.append(zscorescale["z_score"])
    minzscore=min(zscorescalelist)
    maxzscore=max(zscorescalelist)
    rangeval=maxzscore-minzscore
    for zscorescalefinal in originalrawranking:
        zscorescalefinal["scaled_zscore"]=(((zscorescalefinal["z_score"]-minzscore)/rangeval)*25)+25

    for iselfscore in originalrawranking:
        iselfscore["isef_score"]=(iselfscore["scaled_score"]+iselfscore["scaled_zscore"]+iselfscore["scaled_rank"])-50

    projectiselfranking=sorted(projectlist, key = lambda i: i['isef_score'])
    originaliselfranking = [ele for ele in reversed(projectiselfranking)]
    z=1
    for assignirank in originaliselfranking:
            assignirank["iself_rank"]=z
            z=z+1












    paginator_projects = Paginator(originalranking, 10)
    page = request.GET.get('page')
    contacts = paginator_projects.get_page(page)

    if 'createprojects' in request.POST:
       file_path = request.POST.get('filepath')
       try:
        judgesdata=xlrd.open_workbook(file_path)
       except Exception as e:
            data="file does not exist"
            return render(request,'projects_template/listprojects.html',{"projectjson":contacts,"filenotexist":data})

       sheet = judgesdata.sheet_by_index(0)
       judgenames=sheet.cell_value(0,0)

       for judgenum in range(1,sheet.nrows):
            individualjudge=sheet.row_values(judgenum)
            projectinsert = project(project_id=individualjudge[2],project_title=individualjudge[1],project_category=individualjudge[0],description=individualjudge[3])
            projectinsert.save()



    return render(request,'projects_template/listprojects.html',{"projectjson":contacts})
