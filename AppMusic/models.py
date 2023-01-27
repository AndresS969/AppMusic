from django.db import models

# Create your models here.
class Registros(models.Model):
    correo = models.CharField(max_length=25, blank=False, null=True)
    contraseña = models.IntegerField(blank=False, null=True)
    
    def __str__(self) -> str:
        return self.correo