import email
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class DoctorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    sexo= forms.CharField(max_length=10)
    email= forms.EmailField()
    especialidad= forms.CharField(max_length=30)

class PacienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    dni= forms.IntegerField()
    sexo= forms.CharField(max_length=10)
    email= forms.EmailField()
    fechaDeIngreso= forms.DateTimeField()

class TurnoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    doctor= forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    email= forms.EmailField()
    date = forms.DateField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
