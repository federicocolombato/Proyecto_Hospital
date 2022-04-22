import email
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Por favor, reingrese su contraseña', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-Mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['email','password1', 'password2']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    email= forms.EmailField()