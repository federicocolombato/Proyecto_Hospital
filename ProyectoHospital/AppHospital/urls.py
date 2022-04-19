from django.urls import path
from AppHospital import views
from AppHospital.views import listaHospitales

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

]