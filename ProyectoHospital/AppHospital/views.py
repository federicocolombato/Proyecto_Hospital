from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"AppHospital/inicio.html")

def doctor(request):
    return render(request,"AppHospital/doctor.html")

def pacientes(request):
    return render(request,"AppHospital/pacientes.html")

def turnos(request):
    return render(request,"AppHospital/turnos.html")

def sucursales(request):
    return render(request,"AppHospital/sucursales.html")

#def doctor(request):
    #return render(request,"AppHospital/doctor.html")

