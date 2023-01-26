from django.shortcuts import render
from . forms import Formulario


# Create your views here.
def app(request):
    return render(request, "app.html")

#formulario
def formulario(request):
    formulario = Formulario()
    return render(request, "app.html", {"form": formulario})
