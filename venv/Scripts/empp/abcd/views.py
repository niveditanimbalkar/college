from django.shortcuts import render,HttpResponse


# Create your views here.
def welcome(req):
    return HttpResponse('Hello')