from django.db import models
from django.db.models import Model
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
