from django.shortcuts import render
from mi_app.models import Clase1, Clase2, Clase3


def insertar_datos(request):
    # Lógica para insertar datos en los modelos
    return render(request, 'insertar_datos.html')

def buscar_datos(request):
    # Lógica para buscar datos en la base de datos
    return render(request, 'buscar_datos.html')


def home(request):
    return render(request, 'home.html')
