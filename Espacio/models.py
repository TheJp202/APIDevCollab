from django.db import models
from Estacionamiento.models import Estacionamiento

class Espacio(models.Model):
    Estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE,to_field='id',db_column='IdEstacionamiento')
    Numero = models.CharField(max_length=8)
    Estado = models.BooleanField(default=False)
    CostoHora = models.IntegerField(default=1)
    CostoReservaHora = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.Numero} - {self.Estacionamiento}"