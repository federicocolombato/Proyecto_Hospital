from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DoctorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    sexo= forms.CharField(max_length=10)
    email= forms.EmailField()
    especialidad= forms.CharField(max_length=30)

class DateInput(forms.DateInput):
    input_type = 'date'

class TurnoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    doctor= forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    email= forms.EmailField()
    date = forms.DateField()