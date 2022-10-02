from django.shortcuts import render

# Create your views here.

def inicio(recuest):
    return render(recuest, "AppCoder/inicio.html")

def curso(recuest):
    return render(recuest, "AppCoder/curso.html")

def profesor(recuest):
    return render(recuest, "AppCoder/profesor.html")

def estudiante(recuest):
    return render(recuest, "AppCoder/estudiante.html")

def entregable(recuest):
    return render(recuest, "AppCoder/entregable.html")