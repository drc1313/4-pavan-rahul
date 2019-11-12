from django.db import models
from django.db.models import Model
from .project_model import project
class student(Model):
        id=models.CharField(max_length=100 , primary_key=True,blank=False, unique=True)
        firstname=models.CharField(max_length=100)
        lastname=models.CharField(max_length=100)
        school=models.CharField(max_length=100)
        project_id=models.ForeignKey(project, on_delete=models.CASCADE)

        def __str__(self):
            return self.id,self.firstname,self.lastname,self.school,self.project_id
