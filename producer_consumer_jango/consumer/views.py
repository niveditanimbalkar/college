from django.shortcuts import render
import requests
import json
BASE_URI='http://localhost:8000/v1/api/employee/'

class Employee():
    def __init__(self,eid,ename,eorg,esal):
        self.empid=eid
        self.empname=ename
        self.eorgn=eorg
        self.esalary=esal

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)



def get_emp(eid):
    response=requests.get(BASE_URI+str(eid))
    print(response.status_code)
    print( response.json())


def get_all_emp():
    response=requests.get(BASE_URI)
    print(response.status_code)
    print( response.json())

def delete_emp(eid):
    response=requests.delete(BASE_URI+str(eid))
    print(response.status_code)
    if(response.status_code==404):
        print ('Record not found so cannont delete')


def serialize(e):
    values={
        'ID':e.empid,
        'Name':e.empname,
        'Org':e.eorgn,
        'Salary':e.esalary
    }
    return values



def modify_emp(eid):
    pass

def add_emp(dbemp):
    response=requests.post(BASE_URI,json=serialize(dbemp))
    print(response.status_code)
    if (response.status_code==201):
         print('Employee added successfully')



e1=Employee(4,'Shambhavi','PPS',20000)
add_emp(e1)
