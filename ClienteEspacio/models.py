from django.db import models
from Cliente.models import Cliente
from Espacio.models import Espacio

class ClienteEspacio(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,to_field='id',db_column='IdCliente')
    Espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE,to_field='id',db_column='IdEspacio')
    HoraInicio = models.DateTimeField()
    HoraFinal = models.DateTimeField(blank=True, null=True)
    HoraReserva = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.Cliente} - {self.Espacio} - {self.HoraInicio}"