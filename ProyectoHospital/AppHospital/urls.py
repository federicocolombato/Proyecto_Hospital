from django.urls import path
from AppHospital import views

urlpatterns = [
    path('inicio', views.inicio, name ='Inicio'),
    path('doctor', views.doctor, name ='Doctor'),
    path('pacientes', views.pacientes, name ='Pacientes'),
    path('turnos', views.turnos, name ='Turnos'),
    path('sucursales', views.sucursales, name ='Sucursales'),

]