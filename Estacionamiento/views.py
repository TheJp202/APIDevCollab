from django.shortcuts import render
from .models import Estacionamiento
from .serializers import EstacionamientoSerializer
from rest_framework import generics
#from estacionamientos.signals import estacionamiento_ejecutado, estacionamiento_eliminado

class EstacionamientosLCAPIView(generics.ListCreateAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer
    def perform_create(self, serializer):
        estacionamiento = serializer.save()
        #estacionamiento_ejecutado.send(sender=estacionamientos, estacionamiento_id=estacionamiento.id)

class EstacionamientosRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer
    def perform_update(self, serializer):
        estacionamiento = serializer.save()
        #estacionamiento_ejecutado.send(sender=estacionamientos, estacionamiento_id=estacionamiento.id)

    def perform_destroy(self, instance):
        estacionamiento_id = instance.id
        #estacionamiento_eliminado.send(sender=estacionamientos, estacionamiento_id=estacionamiento_id)
        instance.delete()