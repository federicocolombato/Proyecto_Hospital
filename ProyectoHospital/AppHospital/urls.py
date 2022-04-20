from django.urls import path
from AppHospital import views
from AppHospital.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', views.inicio, name ='Inicio'),
    path('doctor', views.doctor, name ='Doctor'),
    path('pacientes', views.pacientes, name ='Pacientes'),
    path('turnos', views.turnos, name ='Turnos'),
    path('sucursales', views.sucursales, name ='Sucursales'),
    path('sucursalesLista', listaHospitales.as_view, name = 'listaHosp'),
    path('sobrenosotros', views.sobreNosotros, name ='SobreNosotros'),
    path('modificarDoctores', views.modificarDoctores, name = "ModificarDoctores"),
    path('eliminarDoctor/<doctor_nombre>/', views.eliminarDoctor, name="EliminarDoctor"),
    path('editarDoctor/<doctor_nombre>/', views.editarDoctor, name="EditarDoctor"),
    path('login/', views.login_request, name = 'Login'),
    path('register/', views.register, name = 'Registro'),
    path('ayuda', views.ayuda, name = 'Ayuda'),
    path('logout/', LogoutView.as_view(template_name= 'templates/AppHospital/logout.html'), name = 'Logout'),
    path('editarPerfil', views.editarPerfil, name = 'Editar Perfil'),


]