from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#inciando vistas
def index(request):
    """primer saludo en django!"""
    return HttpResponse("<h3> Hola mundo!! </h3>")

#vista con parametros
def calcular_mayoria_edad(request, edad: int) -> str:
    if edad >= 18:
        mensaje = "es mayor de edad"
    else:
        mensaje = "es menor de edad!"

    return HttpResponse(f"<h3>{mensaje}</h3>") 

#inciando vistas con templates
def plantilla(request):
    return render(request, "index.html")