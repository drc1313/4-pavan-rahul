from django.db import models
from django.db.models import Model
class judge(Model):
    judge_id=models.CharField( max_length=100,primary_key=True,blank=False, unique=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)

    class Meta:
        db_table = "nhsee_judge"

    def __str__(self):
        return self.judge_id,self.fname,self.lname
