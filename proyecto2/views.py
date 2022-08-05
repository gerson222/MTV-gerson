from asyncore import read
from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from datetime import datetime


def index(self):

    datos_contexto={"fecha_actual": datetime.now, "username": "manolo"}

    plantilla = loader.get_template("index.html")

    documento= plantilla.render(datos_contexto)

    return HttpResponse(documento)

