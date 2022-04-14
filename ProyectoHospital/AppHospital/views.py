from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppHospital.models import Doctor
from AppHospital.forms import DoctorFormulario

# Create your views here.

def inicio(request):
    return render(request,"AppHospital/inicio.html")



def pacientes(request):
    return render(request,"AppHospital/pacientes.html")

def turnos(request):
    return render(request,"AppHospital/turnos.html")

def sucursales(request):
    return render(request,"AppHospital/sucursales.html")

def sobreNosotros(request):
    return render(request,"AppHospital/sobreNosotros.html")

#def doctor(request):
    #return render(request,"AppHospital/doctor.html")

def doctor(request):

      if request.method == 'POST':

            miFormulario = DoctorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  doctor = Doctor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], especialidad=informacion['especialidad']) 

                  doctor.save()

                  return render(request, "AppHospital/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= DoctorFormulario() #Formulario vacio para construir el html

      return render(request, "AppHospital/doctor.html", {"miFormulario":miFormulario})