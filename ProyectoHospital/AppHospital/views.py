from dataclasses import field
from re import template
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppHospital.models import *
from AppHospital.forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

def ayuda(request):
    return render(request,"AppHospital/ayuda.html")

#def doctor(request):
    #return render(request,"AppHospital/doctor.html")

@login_required
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

def leerDoctores(request):

      doctores = Doctor.objects.all() #trae todos los profesores

      contexto= {"doctores":doctores} 

      return render(request, "AppHospital/leerDoctores.html",contexto)


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

@login_required
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

class listaHospitales(ListView):
    model = Sucursales
    template_name = 'templates/AppHospital/sucursalesLista.html'

class PacienteList(ListView):
    model = Paciente
    template = "AppHospital/paciente_list.html"

class PacienteDetalle(DetailView):
    model = Paciente
    template = "AppHospital/paciente_detalle"

class PacienteCreacion(CreateView):
    model = Paciente
    success_url = "/AppHospital/paciente/list"
    fields = '__all__'

class PacienteUpdate(UpdateView):
    model = Paciente
    success_url = "/AppHospital/paciente/list"
    fields = '__all__'

class PacienteDelete(DeleteView):
    model = Paciente
    success_url = "/AppHospital/paciente/list"


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppHospital/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppHospital/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppHospital/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppHospital/login.html", {"form": form})    

#Crear HTML de Registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppHospital/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppHospital/registro.html" ,  {"form":form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "AppHospital/inicio.html")

    
    else: 
        miFormulario = UserEditForm(initial={'email':usuario.email})

    
    return render(request, "AppHospital/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

def buscarPaciente (request):

    return render(request,"AppHospital/buscarPaciente.html")

def buscar(request):

    if request.GET["p"]:

        #mensaje="El paciente: %r" %request.GET['doc']
        dni = request.GET["p"]
        
        paciente = Paciente.objects.filter(dni__icontains=dni)

        return render(request,"AppHospital/buscar.html", {"pacientes":paciente, "dni":dni})

    else:
        mensaje="Intoduce un DNI"

    return HttpResponse(mensaje)




