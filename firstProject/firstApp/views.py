from django.shortcuts import render
from django.http import JsonResponse
from . import models

# Create your views here.

def employeeView(request):
    emp={'id':121,'name':'kiran','sal':1000}

    data=models.Employee.objects.all()
    data={'data':list(data.values())}
    #data={'data':list(data.values('name','salary'))} id will be hidden
    return JsonResponse(data)
