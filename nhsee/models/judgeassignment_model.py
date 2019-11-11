from django.db import models
from django.db.models import Model
class judgeassignment(Model):
            judge_id=models.ForeignKey('judge', models.DO_NOTHING)
            project_id=models.ForeignKey('project',models.DO_NOTHING)
            goal_score=models.FloatField(null=True)
            plan_score=models.FloatField(null=True)
            action_score=models.FloatField(null=True)
            result_analysis_score=models.FloatField(null=True)
            communication_score=models.FloatField(null=True)
            raw_score=models.FloatField(null=True)

            class Meta:
                db_table = "nhsee_judgeassignment"

            def __str__(self):
                return self.judge_id,self.project_id,self.goal_score,self.plan_score,self.action_score,self.result_analysis_score,self.communication_score,self.raw_score
