from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio),
    path("cursos", views.curso), name="Cursos",
    path("profesor", views.profesor),
    path("estudiante", views.estudiante),
    path("entregable", views.entregable),
    
]    