from django.db import models
from datetime import date

class Cliente(models.Model):
    Dni = models.CharField(max_length=8, unique=True)
    Nombre = models.CharField(max_length=50)
    Password = models.CharField(max_length=128)
    FechaRegistro = models.DateField(default=date.today)
    
    def __str__(self):
        return f"{self.Dni} - {self.Nombre}"