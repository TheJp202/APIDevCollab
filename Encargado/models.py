from django.db import models
from datetime import date
from Estacionamiento.models import Estacionamiento
class Encargado(models.Model):
    Dni = models.CharField(max_length=8,unique=True)
    Nombre = models.CharField(max_length=50)
    Password = models.CharField(max_length=128)
    Estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE,to_field='id',db_column='IdEstacionamiento')
    FechaRegistro = models.DateField(default=date.today)
    
    def __str__(self):
        return f"{self.Dni} - {self.Nombre}"