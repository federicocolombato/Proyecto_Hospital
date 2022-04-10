from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Hello, world. You're at the Hospital General index.")

def doctor(request):
    return render(request,"AppHospital/doctor.html")

#def doctor(request):
    #return render(request,"AppHospital/doctor.html")

