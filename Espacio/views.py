from django.shortcuts import render
from .models import Espacio
from .serializers import EspacioSerializer
from rest_framework import generics
#from espacios.signals import espacio_ejecutado, espacio_eliminado

class EspaciosLCAPIView(generics.ListCreateAPIView):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer
    def perform_create(self, serializer):
        espacio = serializer.save()
        #espacio_ejecutado.send(sender=espacios, espacio_id=espacio.id)

class EspaciosRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer
    def perform_update(self, serializer):
        espacio = serializer.save()
        #espacio_ejecutado.send(sender=espacios, espacio_id=espacio.id)

    def perform_destroy(self, instance):
        espacio_id = instance.id
        #espacio_eliminado.send(sender=espacios, espacio_id=espacio_id)
        instance.delete()