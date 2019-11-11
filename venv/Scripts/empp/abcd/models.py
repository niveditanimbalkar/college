from django.db import models

class employee(models.Model):

    empid=models.IntegerField()
    empname=models.CharField(max_length=50)
    empsal=models.FloatField()


