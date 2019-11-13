from django.db import models

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=50)
    eorg=models.CharField(max_length=50)
    esal=models.FloatField()

    class Meta:
        db_table='EmpInfo'

