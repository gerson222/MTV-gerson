from sqlite3 import Cursor
from django.shortcuts import render
from django.http import HttpResponse
from proyectoapp.models import Curso

# Create your views here.

def lista_cursos(request):

    cursos = Curso.objects.all()

    lista_cursos_nombres = []

    for curso in cursos:
        lista_cursos_nombres.append(curso.nombre)

    return HttpResponse(lista_cursos_nombres)