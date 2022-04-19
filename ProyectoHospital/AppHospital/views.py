from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppHospital.models import *
from AppHospital.forms import *

# Create your views here.

def inicio(request):
    return render(request,"AppHospital/inicio.html")

#def pacientes(request):
#    return render(request,"AppHospital/pacientes.html")

#def turnos(request):
#    return render(request,"AppHospital/turnos.html")

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

                  doctor = Doctor (nombre=informacion['nombre'], apellido=informacion['apellido'],sexo=informacion['sexo'],
                   email=informacion['email'], especialidad=informacion['especialidad']) 

                  doctor.save()

                  return render(request, "AppHospital/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= DoctorFormulario() #Formulario vacio para construir el html

      return render(request, "AppHospital/doctor.html", {"miFormulario":miFormulario})

def modificarDoctores(request):

      doctores = Doctor.objects.all() #trae todos los profesores

      contexto= {"doctores":doctores} 

      return render(request, "AppHospital/modificarDoctores.html",contexto)


def eliminarDoctor(request, doctor_nombre):

    doctor = Doctor.objects.get(nombre=doctor_nombre)
    doctor.delete()

    # vuelvo al menú
    doctores = Doctor.objects.all() #trae todos los profesores

    contexto= {"doctores":doctores} 

    return render(request, "AppHospital/modificarDoctores.html", contexto)

def editarDoctor(request, doctor_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    doctor = Doctor.objects.get(nombre=doctor_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = DoctorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            doctor.nombre = informacion['nombre']
            doctor.apellido = informacion['apellido']
            doctor.email = informacion['email']
            doctor.sexo = informacion['sexo']
            doctor.especialidad = informacion['especialidad']

            doctor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppHospital/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = DoctorFormulario(initial={'nombre': doctor.nombre, 'apellido': doctor.apellido,
                                                   'email': doctor.email, 'sexo':doctor.sexo, 'especialidad': doctor.especialidad})

    # Voy al html que me permite editar
    return render(request, "AppHospital/editarDoctor.html", {"miFormulario": miFormulario, "doctor_nombre": doctor_nombre})

def pacientes(request):

    if request.method == 'POST':
    
        miPacienteFormulario = PacienteFormulario(request.POST) #aquí mellega toda la información del html
        
        print(miPacienteFormulario)

        if miPacienteFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miPacienteFormulario.cleaned_data

            paciente = Paciente (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], DNI=informacion['DNI'], sexo=informacion['Sexo'], fechaDeIngreso=informacion['Fecha de Ingreso']) 

            paciente.save()

            return render(request, "AppHospital/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

        miPacienteFormulario= PacienteFormulario() #Formulario vacio para construir el html

    return render(request, "AppHospital/pacientes.html", {"miPacienteFormulario":miPacienteFormulario})

def turnos(request):

      if request.method == 'POST':

            miFormulario = TurnoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  turno = Turno (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  doctor=informacion['doctor'],especilidad=informacion['especialidad'],email=informacion['email'], date=informacion['date']) 

                  turno.save()

                  return render(request, "AppHospital/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TurnoFormulario() #Formulario vacio para construir el html

      return render(request, "AppHospital/turnos.html", {"miFormulario":miFormulario})

