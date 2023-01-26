
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', views.index, name="Hola"),
    path('mayorr/<int:edad>', views.calcular_mayoria_edad, name="mayor"),
    path('plantilla/', views.plantilla, name="plantilla"),
    path('hija/', views.herencia, name="hija"),
]
