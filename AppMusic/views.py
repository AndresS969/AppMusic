from django.shortcuts import render
from . forms import Formulario
from . models import Registros


# Create your views here.
def app(request):
    return render(request, "app.html")

#formulari
def formulario(request):
    formulario = Formulario()
    data_base = Registros()
    if request.POST:
        correo = Formulario()
        Registros.objects.create(correo=request.POST["correo"]).save
    
        

    return render(request, "app.html", {"form": formulario})


    
