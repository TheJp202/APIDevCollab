from django.db import models
from datetime import date

class Estacionamiento(models.Model):
    Nombre = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=128,unique=True)
    FechaRegistro = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.Nombre} - {self.Direccion}"