from django.urls import path
from AppHospital import views

urlpatterns = [
    path('inicio', views.inicio, name ='Inicio'),
    path('doctor', views.doctor, name ='Doctor'),

]