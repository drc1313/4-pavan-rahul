from django.db import models
from django.db.models import Model
import uuid


# Create your models here.
class judge(Model):
    judge_id=models.CharField( max_length=100,primary_key=True,blank=False, unique=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)

    class Meta:
        db_table = "nhsee_judge"

    def __str__(self):
        return self.judge_id,self.fname,self.lname



class project(Model):
    project_id=models.CharField( max_length=100,primary_key=True,blank=False, unique=True)
    description=models.CharField(null=True,max_length=100)
    project_title=models.CharField(null=True,max_length=100)
    project_category=models.CharField(null=True,max_length=100)
    avg_score=models.FloatField(null=True)
    rank=models.IntegerField(null=True)
    z_score=models.FloatField(null=True)
    scaled_score=models.FloatField(null=True)
    scaled_rank=models.IntegerField(null=True)
    scaled_z=models.FloatField(null=True)
    iself_score=models.FloatField(null=True,)
    iself_rank=models.IntegerField(null=True,)
    no_show_project=models.BooleanField(null=True)
    class Meta:
        db_table = 'nhsee_project'

    def __str__(self):
        return self.project_id,self.description,self.project_title,self.project_category,self.avg_score,self.rank,self.z_score,self.scaled_score,self.scaled_rank,self.scaled_z,self.iself_score,self.iself_rank,self.no_show_project


class judge_assignment(Model):
            judge_id=models.ForeignKey('judge', models.DO_NOTHING)
            project_id=models.ForeignKey('project',models.DO_NOTHING)
            goal_score=models.FloatField(null=True)
            plan_score=models.FloatField(null=True)
            action_score=models.FloatField(null=True)
            result_analysis_score=models.FloatField(null=True)
            communication_score=models.FloatField(null=True)
            raw_score=models.FloatField(null=True)

            def __str__(self):
                return self.judge_id,self.project_id,self.goal_score,self.plan_score,self.action_score,self.result_analysis_score,self.communication_score,self.raw_score


class challenge(Model):
    id = models.CharField( max_length=100,primary_key=True,blank=False, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
            return self.id,self.title,self.description

class studet(Model):
        id=models.CharField(max_length=100 , primary_key=True,blank=False, unique=True)
        firstname=models.CharField(max_length=100)
        lastname=models.CharField(max_length=100)
        school=models.CharField(max_length=100)
        project_id=models.ForeignKey(project, on_delete=models.CASCADE)

        def __str__(self):
            return self.id,self.firstname,self.lastname,self.school,self.project_id

# Create your models here.
