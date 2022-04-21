from django.urls import path
from AppHospital import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', views.inicio, name ='Inicio'),
    path('doctor', views.doctor, name ='Doctor'),
    path('pacientes', views.pacientes, name ='Pacientes'),
    path('turnos', views.turnos, name ='Turnos'),
    path('sucursales', views.sucursales, name ='Sucursales'),
    path('sucursalesLista', views.listaHospitales.as_view, name = 'listaHosp'),
    path('sobrenosotros', views.sobreNosotros, name ='SobreNosotros'),
    path('leerDoctores', views.leerDoctores, name = "LeerDoctores"),
    path('eliminarDoctor/<doctor_nombre>/', views.eliminarDoctor, name="EliminarDoctor"),
    path('editarDoctor/<doctor_nombre>/', views.editarDoctor, name="EditarDoctor"),
    path('paciente/list', views.PacienteList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.PacienteDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PacienteCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PacienteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PacienteDelete.as_view(), name='Delete'),
    path('login/', views.login_request, name = 'Login'),
    path('register/', views.register, name = 'Registro'),
    path('ayuda', views.ayuda, name = 'Ayuda'),
    path('logout/', LogoutView.as_view(template_name= 'AppHospital/logout.html'), name = 'Logout'),
    path('editarPerfil', views.editarPerfil, name = 'Editar Perfil'),
    path('buscarPaciente', views.buscarPaciente, name = 'BuscarPaciente'),
    path('buscar/', views.buscar, name = 'Buscar'),


]