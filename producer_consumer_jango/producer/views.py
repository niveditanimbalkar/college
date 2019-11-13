from django.shortcuts import render
from rest_framework import *
from rest_framework_swagger import *
from rest_framework.viewsets import  ModelViewSet
from .models import  Employee
from .serializers import EmployeeSerializers

class EmployeeAPI(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
