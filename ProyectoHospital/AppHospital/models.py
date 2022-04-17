from django.db import models
import datetime
# Create your models here.

class Doctor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    sexo= models.CharField(max_length=10)
    email= models.EmailField()
    especialidad= models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Sexo {self.sexo} - Especialidad {self.especialidad}"

class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni=models.CharField(max_length=15)
    sexo= models.CharField(max_length=10)
    email= models.EmailField()
    fechaDeIngreso= models.DateTimeField('Fecha de Ingreso')
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Sexo {self.sexo} - Fecha de Ingreso {self.fechaDeIngreso}"

class Sucursales(models.Model):
    localidad= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    numero=models.CharField(max_length=15)   
    cantidadDePersonal=models.IntegerField
    def __str__(self):
        return f"Localidad: {self.localidad} - Direccion {self.direccion} - Numero {self.numero} - Empleados {self.cantidadDePersonal}"

class Turno(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    doctor= models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    email= models.EmailField()
    date = models.DateField()
        